# Generated by Django 3.1.4 on 2020-12-29 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')], max_length=400, null=True)),
                ('description', models.CharField(max_length=400, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]