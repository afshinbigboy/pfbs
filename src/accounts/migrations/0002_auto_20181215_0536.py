# Generated by Django 2.1.4 on 2018-12-15 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='std_id',
            field=models.CharField(max_length=9, unique=True, verbose_name='student ID'),
        ),
    ]