# Generated by Django 3.0.2 on 2020-07-25 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200719_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='popular',
            field=models.BooleanField(default=False),
        ),
    ]