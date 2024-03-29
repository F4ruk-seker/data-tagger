# Generated by Django 4.1.3 on 2022-11-27 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authtoken',
            name='id',
        ),
        migrations.AddField(
            model_name='authtoken',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='authtoken',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
