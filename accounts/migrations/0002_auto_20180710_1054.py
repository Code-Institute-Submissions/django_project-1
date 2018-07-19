# Generated by Django 2.0.7 on 2018-07-10 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='numbervalue',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='stringvalue',
        ),
        migrations.AddField(
            model_name='buyer',
            name='city',
            field=models.CharField(default='Dublin', max_length=35),
        ),
        migrations.AddField(
            model_name='buyer',
            name='country',
            field=models.CharField(default='Ireland', max_length=35),
        ),
    ]