# Generated by Django 2.2.7 on 2020-03-21 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_auto_20200321_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_classes', to=settings.AUTH_USER_MODEL),
        ),
    ]
