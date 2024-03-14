# Generated by Django 4.1.10 on 2024-03-12 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_advice_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(blank=True, null=True, upload_to='gallery')),
                ('heading', models.CharField(max_length=100)),
                ('sub_heading', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('service1', models.CharField(max_length=100)),
                ('text1', models.CharField(max_length=500)),
                ('service2', models.CharField(max_length=100)),
                ('text2', models.CharField(max_length=500)),
                ('service3', models.CharField(max_length=100)),
                ('text3', models.CharField(max_length=500)),
                ('service4', models.CharField(max_length=100)),
                ('text4', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Success',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('sub_heading', models.CharField(max_length=100)),
                ('story1', models.CharField(max_length=100)),
                ('text1', models.CharField(max_length=500)),
                ('story2', models.CharField(max_length=100)),
                ('text2', models.CharField(max_length=500)),
                ('story3', models.CharField(max_length=100)),
                ('text3', models.CharField(max_length=500)),
                ('story4', models.CharField(max_length=100)),
                ('text4', models.CharField(max_length=500)),
            ],
        ),
    ]
