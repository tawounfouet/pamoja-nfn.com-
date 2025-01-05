# Generated by Django 5.1.4 on 2025-01-05 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('User', 'Simple utilisateur'), ('Provider', 'Prestataire'), ('Administrator', 'Administrateur'), ('Moderator', 'Modérateur'), ('Staff', 'Staff')], default='User', help_text="Rôle de l'utilisateur", max_length=15),
        ),
    ]
