# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])