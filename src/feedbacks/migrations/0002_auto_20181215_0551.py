# Generated by Django 2.1.4 on 2018-12-15 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
