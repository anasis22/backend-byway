# Generated by Django 5.1.3 on 2024-12-11 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_top_courses_rating_five_out_of'),
    ]

    operations = [
        migrations.AddField(
            model_name='top_courses',
            name='author_icon',
            field=models.ImageField(default='1', upload_to='courses/course_authors'),
            preserve_default=False,
        ),
    ]
