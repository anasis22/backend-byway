# Generated by Django 5.1.3 on 2024-12-11 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_top_courses_course_decription'),
    ]

    operations = [
        migrations.AddField(
            model_name='top_courses',
            name='course_languages',
            field=models.CharField(default='English', max_length=520),
            preserve_default=False,
        ),
    ]
