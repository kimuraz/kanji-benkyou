# Generated by Django 3.1.4 on 2021-01-17 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanjis', '0001_initial'),
        ('quiz', '0002_auto_20210106_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flashcard',
            name='char',
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='kanji',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kanjis.kanji'),
        ),
    ]