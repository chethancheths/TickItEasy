# Generated by Django 4.1.7 on 2023-04-15 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0004_event_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]