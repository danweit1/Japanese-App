# Generated by Django 5.1.3 on 2025-01-10 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grammar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grammar_point', models.CharField(max_length=200)),
                ('meaning', models.TextField(blank=True, null=True)),
                ('usage', models.TextField(blank=True, null=True)),
                ('jlpt_level', models.CharField(choices=[('N1', 'N1'), ('N2', 'N2'), ('N3', 'N3'), ('N4', 'N4'), ('N5', 'N5')], max_length=10)),
            ],
        ),
    ]
