# Generated by Django 3.1.3 on 2020-12-03 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_closet', '0002_remove_closet_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='closet',
            name='name',
            field=models.CharField(default='First Closet', max_length=200),
        ),
    ]