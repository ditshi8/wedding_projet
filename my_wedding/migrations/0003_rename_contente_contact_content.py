# Generated by Django 4.2.3 on 2023-07-25 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_wedding', '0002_contact_alter_article_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contente',
            new_name='content',
        ),
    ]