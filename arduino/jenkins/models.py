# -*- coding:utf-8 -*-
from django.db import models

class Credential(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    credential = models.CharField(max_length=100)


class JenkinsJob(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    credential = models.ForeignKey(Credential, null=True, blank=True)
    url = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.url


class JenkinsJobStatus(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    job = models.ForeignKey(JenkinsJob)
    identifier = models.CharField(max_length=255)
    title =  models.CharField(max_length=255)
    published = models.DateTimeField()
    status = models.BooleanField(default=True)
