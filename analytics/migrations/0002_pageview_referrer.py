# Generated by Django 5.1 on 2024-11-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageview',
            name='referrer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
