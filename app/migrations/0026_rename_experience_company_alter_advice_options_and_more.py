# Generated by Django 4.1.10 on 2024-03-14 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_delete_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Experience',
            new_name='Company',
        ),
        migrations.AlterModelOptions(
            name='advice',
            options={'ordering': ['rating'], 'verbose_name': 'Advice', 'verbose_name_plural': 'Advices'},
        ),
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': 'Banner', 'verbose_name_plural': 'Banners'},
        ),
        migrations.AlterModelOptions(
            name='boxicon',
            options={'verbose_name': 'Box Icon', 'verbose_name_plural': 'Box Icons'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name': 'Contact Us', 'verbose_name_plural': 'Contact Us-s'},
        ),
        migrations.AlterModelOptions(
            name='funfact',
            options={'ordering': ['funfact_count'], 'verbose_name': 'Fun Fact', 'verbose_name_plural': 'Fun Facts'},
        ),
        migrations.AlterModelOptions(
            name='largeboximage',
            options={'verbose_name': 'Large Box Image', 'verbose_name_plural': 'Large Box Images'},
        ),
        migrations.AlterModelOptions(
            name='monthly_price',
            options={'ordering': ['plan_price'], 'verbose_name': 'Monthly_Price', 'verbose_name_plural': 'Monthly_Prices'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.AlterModelOptions(
            name='security',
            options={'verbose_name': 'Security', 'verbose_name_plural': 'Securities'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Service', 'verbose_name_plural': 'Services'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'Slider', 'verbose_name_plural': 'Sliders'},
        ),
        migrations.AlterModelOptions(
            name='success',
            options={'verbose_name': 'Success', 'verbose_name_plural': 'Success-s'},
        ),
        migrations.AlterModelOptions(
            name='testimonial',
            options={'verbose_name': 'Testimonial', 'verbose_name_plural': 'Testimonials'},
        ),
        migrations.AlterModelOptions(
            name='yearly_price',
            options={'ordering': ['plan_price'], 'verbose_name': 'Yearly_Price', 'verbose_name_plural': 'Yearly_Prices'},
        ),
    ]