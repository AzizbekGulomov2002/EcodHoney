# Generated by Django 5.1.3 on 2024-11-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_aboutus_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='contacts',
            field=models.ManyToManyField(to='app.socialmedia'),
        ),
    ]
