# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Key(models.Model):
    room = models.CharField(max_length=50, blank=True, null=True)
    rfid_s = models.CharField(unique=True, max_length=50, blank=True, null=True)
    status = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'key'


class User(models.Model):
    firstname = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    rfid_c = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserKeyLink(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    key = models.ForeignKey(Key, models.DO_NOTHING, blank=True, null=True)
    date_taked = models.DateTimeField(blank=True, null=True)
    date_returned = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_key_link'
