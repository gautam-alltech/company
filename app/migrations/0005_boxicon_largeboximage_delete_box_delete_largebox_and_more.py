# Generated by Django 4.1.10 on 2024-03-11 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_experience_exp_title_content_img1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoxIcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_icon', models.FileField(blank=True, null=True, upload_to='gallery')),
                ('box_heading', models.CharField(max_length=200)),
                ('box_text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LargeBoxImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_icon', models.FileField(blank=True, null=True, upload_to='gallery')),
                ('box_heading', models.CharField(max_length=200)),
                ('box_text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Box',
        ),
        migrations.DeleteModel(
            name='LargeBox',
        ),
        migrations.RemoveField(
            model_name='content',
            name='img2',
        ),
        migrations.AlterField(
            model_name='contactus',
            name='contact_phone',
            field=models.CharField(default='+91 0000000000', max_length=15),
        ),
        migrations.AlterField(
            model_name='content',
            name='img1',
            field=models.FileField(blank=True, null=True, upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='content',
            name='sub_title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='exp_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='exp_year',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='funfact',
            name='funfact_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='header',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_img',
            field=models.FileField(blank=True, null=True, upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='logo_hover',
            field=models.FileField(blank=True, null=True, upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='test_img',
            field=models.FileField(blank=True, null=True, upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='test_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
