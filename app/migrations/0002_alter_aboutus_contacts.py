# Generated by Django 5.1.3 on 2024-11-23 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='contacts',
            field=models.ManyToManyField(blank=True, null=True, to='app.socialmedia'),
        ),
    ]