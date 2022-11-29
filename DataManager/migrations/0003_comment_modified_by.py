# Generated by Django 4.1.3 on 2022-11-29 02:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DataManager', '0002_reviews_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='modified_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
