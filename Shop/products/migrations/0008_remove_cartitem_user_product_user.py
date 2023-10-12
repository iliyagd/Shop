# Generated by Django 4.2.4 on 2023-09-09 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0007_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='User',
        ),
        migrations.AddField(
            model_name='product',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
