# Generated by Django 3.2.16 on 2023-10-02 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_follow_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='follow',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]