# Generated by Django 4.2.4 on 2023-09-05 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_articleserach_search'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Search',
            new_name='ArticleSerachLog',
        ),
    ]
