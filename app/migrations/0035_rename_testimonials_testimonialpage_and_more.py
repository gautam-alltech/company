# Generated by Django 4.1.10 on 2024-03-19 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_testimonials'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Testimonials',
            new_name='TestimonialPage',
        ),
        migrations.AlterModelOptions(
            name='testimonialpage',
            options={'verbose_name': 'TestimonialPage', 'verbose_name_plural': 'TestimonialPages'},
        ),
    ]
