# Generated by Django 4.2.1 on 2023-08-28 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbvapp', '0004_school_medium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='medium',
            field=models.CharField(default='English', max_length=100),
        ),
    ]