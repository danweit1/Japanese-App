# Generated by Django 5.1.3 on 2025-01-09 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanji_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kanji',
            name='common_words',
            field=models.TextField(blank=True, help_text='Common words using this kanji', null=True),
        ),
    ]
