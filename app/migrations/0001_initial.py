# Generated by Django 4.1.10 on 2024-03-07 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_icon', models.ImageField(upload_to='')),
                ('box_heading', models.TextField()),
                ('box_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_heading', models.TextField()),
                ('contact_sub_heading', models.TextField()),
                ('contact_phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('sub_title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_heading', models.TextField()),
                ('exp_year', models.TextField()),
                ('exp_text', models.TextField()),
                ('exp_title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FunFact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funfact_title', models.TextField()),
                ('funfact_count', models.IntegerField()),
                ('funfact_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=50)),
                ('logo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='LargeBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_icon', models.ImageField(upload_to='')),
                ('box_heading', models.TextField()),
                ('box_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_img', models.ImageField(upload_to='')),
                ('project_heading', models.TextField()),
                ('project_category', models.TextField()),
                ('project_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.TextField()),
                ('section_heading', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
                ('logo_hover', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_subject', models.TextField()),
                ('test_text', models.TextField()),
                ('test_img', models.ImageField(upload_to='')),
                ('test_name', models.TextField()),
                ('test_post', models.TextField()),
            ],
        ),
    ]