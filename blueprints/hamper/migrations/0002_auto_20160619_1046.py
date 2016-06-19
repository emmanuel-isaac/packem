# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hamper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemHamperLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_quantity', models.IntegerField(default=1, null=True)),
                ('hamper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamper.Hamper')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamper.Item')),
            ],
        ),
        migrations.DeleteModel(
            name='ItemHamper',
        ),
        migrations.AddField(
            model_name='hamper',
            name='items',
            field=models.ManyToManyField(through='hamper.ItemHamperLine', to='hamper.Item'),
        ),
        migrations.AlterUniqueTogether(
            name='itemhamperline',
            unique_together=set([('item', 'hamper')]),
        ),
    ]
