# Generated by Django 3.1.4 on 2020-12-31 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_auto_20201230_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='minutes',
            new_name='timeItWillTake',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
    ]