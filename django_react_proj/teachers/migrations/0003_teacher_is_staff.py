# Generated by Django 4.1.2 on 2022-10-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]