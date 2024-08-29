# Generated by Django 5.1 on 2024-08-26 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='connect/photos')),
                ('content', models.TextField()),
                ('URL', models.URLField()),
            ],
        ),
    ]
