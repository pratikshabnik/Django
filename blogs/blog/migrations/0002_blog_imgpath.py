# Generated by Django 4.1.1 on 2022-10-19 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='imgpath',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
