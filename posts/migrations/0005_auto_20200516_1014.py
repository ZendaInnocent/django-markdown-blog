# Generated by Django 3.0.3 on 2020-05-16 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_excerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(max_length=100),
        ),
    ]
