# Generated by Django 4.0.5 on 2022-06-16 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_remove_table_guid_table_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitems',
            name='item_image',
            field=models.ImageField(upload_to='food'),
        ),
    ]
