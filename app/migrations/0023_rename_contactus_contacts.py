# Generated by Django 4.1.10 on 2024-03-13 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_content_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactUs',
            new_name='Contacts',
        ),
    ]