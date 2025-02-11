# Generated by Django 5.1.4 on 2025-01-04 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates', models.JSONField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]
