# Generated by Django 4.1.4 on 2023-01-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_remove_archdesregisterdb_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='archdesregisterdb',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
