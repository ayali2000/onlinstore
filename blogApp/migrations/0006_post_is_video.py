# Generated by Django 4.1 on 2022-10-10 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0005_remove_post_body_alter_more_post_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_Video',
            field=models.BooleanField(default=False),
        ),
    ]
