# Generated by Django 4.2.9 on 2024-03-14 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Проданный товар', 'verbose_name_plural': 'Проданные товары'},
        ),
    ]
