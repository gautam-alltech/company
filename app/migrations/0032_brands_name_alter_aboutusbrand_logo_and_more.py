# Generated by Django 5.0.3 on 2024-03-18 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_aboutusbrand_aboutusfunfact_aboutussolution_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='aboutusbrand',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='about_us/gallery'),
        ),
        migrations.AlterField(
            model_name='aboutusbrand',
            name='logo_hover',
            field=models.FileField(blank=True, null=True, upload_to='about_us/gallery'),
        ),
        migrations.AlterField(
            model_name='aboutusstory',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='about_us/gallery'),
        ),
        migrations.AlterField(
            model_name='aboutustestimonial',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='about_us/gallery'),
        ),
        migrations.AlterField(
            model_name='advice',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='advices/gallery'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='banner/gallery'),
        ),
        migrations.AlterField(
            model_name='boxicon',
            name='box_icon',
            field=models.FileField(blank=True, null=True, upload_to='boxes/gallery'),
        ),
        migrations.AlterField(
            model_name='brands',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='brands/gallery'),
        ),
        migrations.AlterField(
            model_name='brands',
            name='logo_hover',
            field=models.FileField(blank=True, null=True, upload_to='brands/gallery'),
        ),
        migrations.AlterField(
            model_name='downmember',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='members/gallery'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='gallery/gallery'),
        ),
        migrations.AlterField(
            model_name='largeboximage',
            name='box_icon',
            field=models.FileField(blank=True, null=True, upload_to='largeboxes/gallery'),
        ),
        migrations.AlterField(
            model_name='monthly_price',
            name='plan_img',
            field=models.FileField(blank=True, null=True, upload_to='prices/gallery'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_img',
            field=models.FileField(blank=True, null=True, upload_to='projects/gallery'),
        ),
        migrations.AlterField(
            model_name='service',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='services/gallery'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='img1',
            field=models.FileField(blank=True, null=True, upload_to='slider/gallery'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='img2',
            field=models.FileField(blank=True, null=True, upload_to='slider/gallery'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='testimonials/gallery'),
        ),
        migrations.AlterField(
            model_name='topmember',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='members/gallery'),
        ),
        migrations.AlterField(
            model_name='yearly_price',
            name='plan_img',
            field=models.FileField(blank=True, null=True, upload_to='prices/gallery'),
        ),
    ]
