# Generated by Django 4.1.4 on 2023-08-14 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_sellerprofile_type_sellerprofile_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sellerprofile',
            old_name='phone',
            new_name='bakeryPhone',
        ),
    ]
