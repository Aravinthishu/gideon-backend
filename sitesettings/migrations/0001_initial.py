# Generated by Django 5.1.5 on 2025-01-27 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('googlemap_url', models.CharField(blank=True, max_length=1000, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='sitesettings/')),
                ('fevicon', models.ImageField(blank=True, null=True, upload_to='sitesettings/')),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Social_links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='sitesettings/social_links')),
            ],
        ),
    ]
