# Generated by Django 5.0.4 on 2024-05-10 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_profile_facebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]