# Generated by Django 4.1.4 on 2023-01-03 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_alter_archdesregisterdb_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archdesregisterdb',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
