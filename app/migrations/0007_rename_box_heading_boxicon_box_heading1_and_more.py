# Generated by Django 4.1.10 on 2024-03-11 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_box_icon_boxicon_box_icon1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boxicon',
            old_name='box_heading',
            new_name='box_heading1',
        ),
        migrations.RenameField(
            model_name='boxicon',
            old_name='box_text',
            new_name='box_text1',
        ),
        migrations.RenameField(
            model_name='largeboximage',
            old_name='box_heading',
            new_name='box_heading1',
        ),
        migrations.RenameField(
            model_name='largeboximage',
            old_name='box_text',
            new_name='box_text1',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_category',
            new_name='project_category1',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_heading',
            new_name='project_category2',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_text',
            new_name='project_text1',
        ),
        migrations.RenameField(
            model_name='testimonial',
            old_name='test_name',
            new_name='test_name1',
        ),
        migrations.RenameField(
            model_name='testimonial',
            old_name='test_post',
            new_name='test_name2',
        ),
        migrations.RenameField(
            model_name='testimonial',
            old_name='test_subject',
            new_name='test_name3',
        ),
        migrations.RenameField(
            model_name='testimonial',
            old_name='test_text',
            new_name='test_text1',
        ),
        migrations.AddField(
            model_name='boxicon',
            name='box_heading2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boxicon',
            name='box_heading3',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boxicon',
            name='box_text2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='boxicon',
            name='box_text3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='largeboximage',
            name='box_heading2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='largeboximage',
            name='box_heading3',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='largeboximage',
            name='box_text2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='largeboximage',
            name='box_text3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_category3',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='project_category4',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='project_heading1',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='project_heading2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='project_heading3',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='project_heading4',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='project_text2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_text3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_text4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='test_name4',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimonial',
            name='test_post1',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimonial',
            name='test_post2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimonial',
            name='test_post3',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimonial',
            name='test_post4',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimonial',
            name='test_subject1',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimonial',
            name='test_subject2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimonial',
            name='test_subject3',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimonial',
            name='test_subject4',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimonial',
            name='test_text2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='test_text3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='test_text4',
            field=models.TextField(blank=True, null=True),
        ),
    ]
