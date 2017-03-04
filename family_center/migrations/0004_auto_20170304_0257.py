# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-04 02:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family_center', '0003_auto_20170217_0625'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_type', models.CharField(choices=[(b'M', b'monthly'), (b'Y', b'Yearly')], default='M', max_length=16)),
                ('total', models.FloatField()),
                ('year', models.IntegerField(blank=True, null=True)),
                ('month', models.CharField(blank=True, choices=[(b'1', b'January'), (b'2', b'February'), (b'3', b'March'), (b'4', b'April'), (b'5', b'May'), (b'6', b'June'), (b'7', b'July'), (b'8', b'August'), (b'9', b'September'), (b'10', b'October'), (b'11', b'November'), (b'12', b'December')], max_length=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MemberBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('paid', models.BooleanField(default=False)),
                ('paid_date', models.DateTimeField(null=True)),
                ('family_bill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='family_center.FamilyBill')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='family_center.Member')),
            ],
        ),
        migrations.RemoveField(
            model_name='bill',
            name='fum',
        ),
        migrations.RemoveField(
            model_name='family',
            name='admin',
        ),
        migrations.AddField(
            model_name='family',
            name='description',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='family',
            name='provider',
            field=models.CharField(blank=True, choices=[(b'T-MOBILE', b'T-Mobile')], max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='familyusermapping',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='familyusermapping',
            name='family',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='family_center.Family'),
        ),
        migrations.AlterField(
            model_name='familyusermapping',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='family_center.Member'),
        ),
        migrations.DeleteModel(
            name='Bill',
        ),
        migrations.AddField(
            model_name='familybill',
            name='family',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='family_center.Family'),
        ),
    ]
