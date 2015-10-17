# -*- coding:utf-8 -*-
from __future__ import absolute_import
from datetime import timedelta

from celery.task import periodic_task

import feedparser
from jenkins.models import JenkinsJob, JenkinsJobStatus
from celery.decorators import periodic_task


@periodic_task(run_every=timedelta(seconds=15))
def verify_jenkins():
    success = True
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
                    identifier=entry.id
                )

    return success
