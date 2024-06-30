from django.db import models
from django.contrib.auth.models import User


class Scanner(models.Model):
    owner = models.ManyToManyField(User, related_name='scanner', blank=True)
    name = models.CharField(max_length=255, default='Please Rename')
    accountNumber = models.CharField(max_length=255, unique=True)
    brokerName = models.CharField(max_length=255, null=True, blank=True)
    currentEquity = models.FloatField(null=True, blank=True)
    totalSwap = models.FloatField(null=True, blank=True)
    longSwap = models.FloatField(null=True, blank=True)
    shortSwap = models.FloatField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    message = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('accountNumber', 'name')
