# Generated by Django 2.2.6 on 2019-10-24 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=250)),
                ('site_url', models.URLField()),
                ('description', models.TextField()),
                ('tags', models.CharField(max_length=2000)),
                ('youtube', models.URLField()),
                ('facebook', models.URLField()),
                ('twiiter', models.URLField()),
                ('google', models.URLField()),
                ('logo', models.ImageField(upload_to='logo')),
                ('maintaince_mode', models.BooleanField()),
            ],
        ),
    ]
