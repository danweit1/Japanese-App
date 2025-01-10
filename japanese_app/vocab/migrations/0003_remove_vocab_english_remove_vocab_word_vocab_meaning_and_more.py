# Generated by Django 5.1.3 on 2025-01-10 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0002_remove_vocab_meaning_remove_vocab_reading_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vocab',
            name='english',
        ),
        migrations.RemoveField(
            model_name='vocab',
            name='word',
        ),
        migrations.AddField(
            model_name='vocab',
            name='meaning',
            field=models.TextField(default='No meaning provided'),
        ),
        migrations.AddField(
            model_name='vocab',
            name='original',
            field=models.CharField(default='No value provided', max_length=255),
        ),
        migrations.AlterField(
            model_name='vocab',
            name='jlpt_level',
            field=models.CharField(default='N5', max_length=10),
        ),
    ]