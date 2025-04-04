# Generated by Django 5.1.6 on 2025-03-15 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('subject', models.CharField(max_length=350)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='participant',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='participants', to='events.event'),
        ),
    ]
