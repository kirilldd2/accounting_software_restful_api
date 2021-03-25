# Generated by Django 3.1.7 on 2021-03-25 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_auto_20210325_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='vedomost',
            name='doc_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='report',
            name='doc_num',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reportline',
            name='produced',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vedomost',
            name='creation_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='vedomostline',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
