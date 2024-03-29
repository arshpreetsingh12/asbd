# Generated by Django 2.2.6 on 2019-10-25 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('Zip', models.CharField(max_length=15)),
                ('telephone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('profile_pic', models.ImageField(upload_to='media')),
            ],
        ),
    ]
