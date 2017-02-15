# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-04 07:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family_center', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=256)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='period',
            name='family',
        ),
        migrations.RemoveField(
            model_name='periodfumapping',
            name='fum',
        ),
        migrations.RemoveField(
            model_name='periodfumapping',
            name='period',
        ),
        migrations.RemoveField(
            model_name='familyusermapping',
            name='family_id',
        ),
        migrations.RemoveField(
            model_name='familyusermapping',
            name='user_id',
        ),
        migrations.AddField(
            model_name='familyusermapping',
            name='family',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fu', to='family_center.Family'),
        ),
        migrations.AddField(
            model_name='familyusermapping',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fu', to='family_center.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='family',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family', to='family_center.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='facebook_id',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.DeleteModel(
            name='Period',
        ),
        migrations.DeleteModel(
            name='PeriodFUMapping',
        ),
        migrations.AddField(
            model_name='bill',
            name='fum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pfu', to='family_center.FamilyUserMapping'),
        ),
    ]