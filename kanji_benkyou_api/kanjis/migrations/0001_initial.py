# Generated by Django 3.1.4 on 2021-01-17 17:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kanji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kanji', models.CharField(max_length=5)),
                ('grade', models.IntegerField(null=True)),
                ('heisig_en', models.CharField(max_length=100, null=True)),
                ('jlpt', models.IntegerField(null=True)),
                ('kun_readings', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), null=True, size=None)),
                ('meanings', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), null=True, size=None)),
                ('name_readings', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), null=True, size=None)),
                ('on_readings', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), null=True, size=None)),
                ('stroke_count', models.IntegerField(null=True)),
                ('unicode_code', models.CharField(max_length=5)),
            ],
        ),
    ]
