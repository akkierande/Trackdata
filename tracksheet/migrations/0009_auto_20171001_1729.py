# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 11:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracksheet', '0008_auto_20170923_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_status', models.CharField(choices=[('Unlabelled', 'Unlabelled'), ('Paused', 'Paused'), ('Labelled', 'Labelled'), ('Corrected', 'Corrected'), ('Completed', 'Completed'), ('Uploaded', 'Uploaded'), ('ChangeNeeded', 'ChangeNeeded')], default='Unlabelled', max_length=15)),
                ('checkout_at', models.DateTimeField(blank=True, null=True)),
                ('image_objects', models.IntegerField(blank=True, null=True)),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
                ('time_on_image', models.TimeField(blank=True, null=True)),
                ('checkout_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='project',
            old_name='challanges',
            new_name='challenges',
        ),
        migrations.RemoveField(
            model_name='image',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='image',
            name='corrected_by',
        ),
        migrations.RemoveField(
            model_name='image',
            name='correction_date',
        ),
        migrations.RemoveField(
            model_name='image',
            name='correction_time',
        ),
        migrations.RemoveField(
            model_name='image',
            name='correction_time_2',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_objects',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_status',
        ),
        migrations.RemoveField(
            model_name='image',
            name='label_rating',
        ),
        migrations.RemoveField(
            model_name='image',
            name='labeldate',
        ),
        migrations.RemoveField(
            model_name='image',
            name='labelled_by',
        ),
        migrations.RemoveField(
            model_name='image',
            name='labeltime',
        ),
        migrations.AddField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='image',
            name='created_by',
            field=models.CharField(default='admin', max_length=20),
        ),
        migrations.AddField(
            model_name='image',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='image',
            name='updated_by',
            field=models.CharField(default='admin', max_length=20),
        ),
        migrations.AddField(
            model_name='package',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='package',
            name='created_by',
            field=models.CharField(default='admin', max_length=20),
        ),
        migrations.AddField(
            model_name='package',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='package',
            name='updated_by',
            field=models.CharField(default='admin', max_length=20),
        ),
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='project',
            name='created_by',
            field=models.CharField(default='admin', max_length=20),
        ),
        migrations.AddField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='project',
            name='updated_by',
            field=models.CharField(default='admin', max_length=20),
        ),
        migrations.AlterField(
            model_name='package',
            name='package_status',
            field=models.CharField(choices=[('Unlabelled', 'Unlabelled'), ('Label', 'Labelled'), ('Corrected', 'Corrected'), ('Uploaded', 'Uploaded')], default='Unlabelled', max_length=15),
        ),
        migrations.AlterField(
            model_name='package',
            name='total_image',
            field=models.IntegerField(default='00000', null=True),
        ),
        migrations.AddField(
            model_name='checkout',
            name='image_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracksheet.Image'),
        ),
    ]
