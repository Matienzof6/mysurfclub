# Generated by Django 4.2.3 on 2023-07-26 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_alter_member_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='members'),
        ),
    ]
