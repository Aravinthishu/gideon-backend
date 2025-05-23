# Generated by Django 5.1.5 on 2025-03-04 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Awards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('position', models.CharField(blank=True, max_length=250, null=True)),
                ('testimonial', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='award',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
