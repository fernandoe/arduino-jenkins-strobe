# -*- coding:utf-8 -*-
from __future__ import absolute_import
from datetime import timedelta
import sys
import glob

from celery.task import periodic_task
import dateutil.parser
import feedparser
import serial

from jenkins.models import JenkinsJob, JenkinsJobStatus
from celery.decorators import periodic_task
from django.conf import settings




@periodic_task(run_every=timedelta(seconds=25))
def verify_jenkins():
    jobs = JenkinsJob.objects.filter(active=True)
    for job in jobs:
        url = job.url
        if job.credential:
            url = url.replace('https://', 'https://%s@')
            url = url % (job.credential.credential)

        feed = feedparser.parse(url)
        for entry in feed.entries:
            jjs = JenkinsJobStatus.objects.filter(identifier=entry.id)
            if jjs.count() == 0:
                JenkinsJobStatus.objects.create(
                    job=job,
                    identifier=entry.id,
                    title=entry.title,
                    published=dateutil.parser.parse(entry.published),
                    status=entry.title.find('broken') < 0
                )
    return True


@periodic_task(run_every=timedelta(seconds=30))
def send_to_usb():
    success = True
    jobs = JenkinsJob.objects.filter(active=True)
    for job in jobs:
        status = JenkinsJobStatus.objects.filter(job=job).order_by('-published')[0].status
        if status is False:
            success = False
            break

    ser = settings.SERIAL
    if success:
        ser.write('b')
    else:
        ser.write('a')

    return success


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result
