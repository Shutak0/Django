# Generated by Django 4.1 on 2022-10-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_theme_comment_post_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='d', max_length=200),
            preserve_default=False,
        ),
    ]
