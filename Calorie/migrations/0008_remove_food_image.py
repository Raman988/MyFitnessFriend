# Generated by Django 3.2.9 on 2022-06-06 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Calorie', '0007_delete_record'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='image',
        ),
    ]