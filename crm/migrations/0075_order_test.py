# Generated by Django 3.1.4 on 2021-01-06 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0074_order_streak'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='test',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
