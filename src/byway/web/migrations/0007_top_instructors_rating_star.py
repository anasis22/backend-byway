# Generated by Django 5.1.3 on 2024-12-10 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_customer_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='top_instructors',
            name='rating_star',
            field=models.ImageField(default='1', upload_to='instructors/rating_stars'),
            preserve_default=False,
        ),
    ]
