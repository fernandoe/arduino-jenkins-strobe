# -*- coding:utf-8 -*-
from jenkins.models import Credential, JenkinsJob, JenkinsJobStatus
from django.contrib import admin


from django import forms
class CredentialForm(forms.ModelForm):
    class Meta:
        model = Credential
        fields = '__all__'
        widgets = {
        'credential': forms.PasswordInput(),
    }

class CredentialModelAdmin(admin.ModelAdmin):
    list_display = ['id']
    form = CredentialForm
admin.site.register(Credential, CredentialModelAdmin)

class JenkinsJobModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'url', 'active']
admin.site.register(JenkinsJob, JenkinsJobModelAdmin)


class JenkinsJobStatusModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'job', 'status']
admin.site.register(JenkinsJobStatus, JenkinsJobStatusModelAdmin)
