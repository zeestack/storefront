# Generated by Django 3.2.9 on 2021-11-24 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='given_name',
        ),
        migrations.RemoveField(
            model_name='address',
            name='zip_code',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.AlterField(
            model_name='customer',
            name='given_name',
            field=models.CharField(db_column='first_name', max_length=255),
        ),
    ]