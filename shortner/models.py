from django.db import models


class Url(models.Model):
    link = models.CharField(max_length=255)
    uuid = models.CharField(max_length=10)
