# Generated by Django 4.0.4 on 2022-05-01 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_category_category_slug_alter_part_part_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_slug',
            field=models.SlugField(max_length=250, verbose_name='slug поле подкатегории'),
        ),
    ]