# Generated by Django 5.0.4 on 2024-04-10 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menu_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
