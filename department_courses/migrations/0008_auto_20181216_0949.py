# Generated by Django 2.1.2 on 2018-12-16 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department_courses', '0007_auto_20181216_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]