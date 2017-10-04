# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracksheet', '0004_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='created_by',
            field=models.CharField(default='admin', max_length=20),
        ),
        migrations.AddField(
            model_name='employee',
            name='dob',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='fullname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='updated_by',
            field=models.CharField(default='admin', max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='education',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.IntegerField(default='00000', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='experience',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='project',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='shift',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
