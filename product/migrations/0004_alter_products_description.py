# Generated by Django 5.1.5 on 2025-03-12 06:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
