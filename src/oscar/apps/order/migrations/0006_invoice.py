# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-07 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0005_legalentity_legalentityaddress'),
        ('order', '0005_update_email_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=128, verbose_name='Invoice number')),
                ('notes', models.TextField(null=True, verbose_name='Notes for invoice')),
                ('document', models.FileField(blank=True, max_length=255, null=True, upload_to='invoices/%Y/%m/', verbose_name='Document')),
                ('legal_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='partner.LegalEntity', verbose_name='Legal Entity')),
                ('order', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoice', to='order.Order', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoices',
                'abstract': False,
            },
        ),
    ]
