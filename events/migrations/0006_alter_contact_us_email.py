# Generated by Django 5.1.6 on 2025-03-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_remove_contact_us_subject_contact_us_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
