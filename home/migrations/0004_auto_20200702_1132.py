# Generated by Django 3.0.7 on 2020-07-02 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200702_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.IntegerField(default=100, max_length=50),
        ),
    ]