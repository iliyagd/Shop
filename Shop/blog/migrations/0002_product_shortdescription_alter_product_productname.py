# Generated by Django 4.2.4 on 2023-08-18 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ShortDescription',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='ProductName',
            field=models.CharField(max_length=200),
        ),
    ]