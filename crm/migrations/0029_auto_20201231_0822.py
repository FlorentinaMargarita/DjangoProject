# Generated by Django 3.1.4 on 2020-12-31 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0028_auto_20201231_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='checked',
            field=models.CharField(blank=True, choices=[('Check', 'Check')], max_length=200, null=True),
        ),
    ]
