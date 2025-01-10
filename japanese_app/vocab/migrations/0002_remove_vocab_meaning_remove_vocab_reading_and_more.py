# Generated by Django 5.1.3 on 2025-01-10 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vocab',
            name='meaning',
        ),
        migrations.RemoveField(
            model_name='vocab',
            name='reading',
        ),
        migrations.AddField(
            model_name='vocab',
            name='english',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vocab',
            name='furigana',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='vocab',
            name='jlpt_level',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='vocab',
            name='word',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]