# Generated by Django 2.1.4 on 2018-12-27 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object_adder', '0005_auto_20181227_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='img',
            field=models.ImageField(blank=True, default='/images/None/nopic.svg', upload_to='images/'),
        ),
    ]