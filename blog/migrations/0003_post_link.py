# Generated by Django 2.0.9 on 2019-01-06 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(default='https://hairways.co.ke', max_length=500),
        ),
    ]
