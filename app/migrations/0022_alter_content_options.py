# Generated by Django 4.1.10 on 2024-03-13 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_yearly_price_rename_price_monthly_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['title'], 'verbose_name': 'Content', 'verbose_name_plural': 'Contents'},
        ),
    ]
