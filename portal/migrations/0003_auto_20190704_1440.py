# Generated by Django 2.2.2 on 2019-07-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_customuser_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(default='Full Name', max_length=41, verbose_name='full name'),
        ),
    ]