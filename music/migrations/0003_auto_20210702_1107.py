# Generated by Django 3.1.2 on 2021-07-02 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='mobile',
        ),
        migrations.AddField(
            model_name='detail',
            name='dept',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
