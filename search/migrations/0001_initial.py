# Generated by Django 5.1.4 on 2025-01-26 20:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=255)),
                ('filters', models.JSONField(default=dict)),
                ('results_count', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='search_history', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'search histories',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='SearchDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('search_text', models.TextField(blank=True, null=True)),
                ('tags', models.JSONField(default=list)),
                ('location', models.JSONField(null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'indexes': [models.Index(fields=['title', 'content'], name='search_sear_title_71219a_idx')],
            },
        ),
    ]
