# Generated by Django 3.1.4 on 2020-12-31 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0017_remove_order_timeitwilltake'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='checked',
            field=models.IntegerField(default=0),
        ),
    ]
