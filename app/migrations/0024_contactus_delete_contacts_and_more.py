# Generated by Django 4.1.10 on 2024-03-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_rename_contactus_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(default='+91 0000000000', max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='address',
            new_name='contact_heading',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='contact_phone',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='location',
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_sub_heading',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]