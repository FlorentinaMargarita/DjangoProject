# Generated by Django 3.1.4 on 2021-01-03 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0058_auto_20210103_0752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='count',
            name='order',
        ),
        migrations.RemoveField(
            model_name='repeats',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='checkedList',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.repeats'),
        ),
        migrations.AddField(
            model_name='order',
            name='strikeList',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.count'),
        ),
    ]
