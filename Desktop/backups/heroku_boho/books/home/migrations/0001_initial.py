# Generated by Django 3.0.2 on 2020-07-05 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('dec', models.CharField(max_length=50)),
                ('standard', models.CharField(max_length=50)),
                ('pattern', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('bookfront_cover', models.ImageField(default='picc', upload_to='pics')),
                ('bookback_cover', models.ImageField(default='picc', upload_to='pics')),
                ('index_1', models.ImageField(default='picc', upload_to='pics')),
                ('index_2', models.ImageField(default='picc', upload_to='pics')),
                ('index_3', models.ImageField(default='picc', upload_to='pics')),
                ('index_4', models.ImageField(default='picc', upload_to='pics')),
            ],
        ),
    ]