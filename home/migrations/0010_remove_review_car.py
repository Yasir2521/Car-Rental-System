# Generated by Django 5.0.2 on 2024-04-19 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_contact_phone_number_contact_reply_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='car',
        ),
    ]
