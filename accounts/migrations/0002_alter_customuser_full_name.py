# Generated by Django 4.0.4 on 2022-05-11 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(max_length=90, verbose_name='ФИО'),
        ),
    ]
