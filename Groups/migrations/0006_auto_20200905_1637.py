# Generated by Django 3.1.1 on 2020-09-05 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Groups', '0005_auto_20200905_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(upload_to='groups/'),
        ),
    ]
