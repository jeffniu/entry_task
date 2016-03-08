# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        db_table = 'django_migrations'


class TbToken(models.Model):
    user = models.ForeignKey('TbUser', models.DO_NOTHING, blank=True, null=True)
    token = models.CharField(max_length=64, blank=True, null=True)
    creation_time = models.DateTimeField()

    class Meta:
        db_table = 'tb_token'


class TbUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20, blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    icon = models.CharField(max_length=30, blank=True, null=True)
    pwd = models.CharField(max_length=64, blank=True, null=True)
    creation_time = models.DateTimeField()

    class Meta:
        db_table = 'tb_user'
