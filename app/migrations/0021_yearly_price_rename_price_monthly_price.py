# Generated by Django 4.1.10 on 2024-03-13 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_remove_price_sub_title_remove_price_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yearly_Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=100)),
                ('plan_img', models.FileField(blank=True, null=True, upload_to='gallery')),
                ('plan_currency', models.CharField(default='$', max_length=20)),
                ('plan_price', models.CharField(max_length=10)),
                ('plan_period', models.CharField(max_length=50)),
                ('plan_list_item1', models.CharField(max_length=100)),
                ('plan_list_item2', models.CharField(max_length=100)),
                ('plan_list_item3', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Price',
            new_name='Monthly_Price',
        ),
    ]