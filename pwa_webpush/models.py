from django.db import models
from django.core.exceptions import FieldError
from django.conf import settings

from django.db.models import DO_NOTHING


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)


class SubscriptionInfo(models.Model):
    browser = models.CharField(max_length=100)
    endpoint = models.URLField(max_length=255)
    auth = models.CharField(max_length=100)
    p256dh = models.CharField(max_length=100)


class PushInformation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='webpush_info', blank=True, null=True,
                             on_delete=models.CASCADE)
    subscription = models.ForeignKey(SubscriptionInfo, related_name='webpush_info', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='webpush_info', blank=True, null=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Check whether user or the group field is present
        # At least one field should be present there
        # Through from the functionality its not possible, just in case! ;)
        if self.user or self.group:
            super(PushInformation, self).save(*args, **kwargs)
        else:
            raise FieldError('At least user or group should be present')


class PushMessage(models.Model):
    active = models.BooleanField(default=True)
    send_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=200, null=False, default='Message from ProAct Rx.')
    message = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    icon = models.URLField(blank=True, null=True)
    send_to = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=DO_NOTHING)
    sent = models.BooleanField(default=False)
