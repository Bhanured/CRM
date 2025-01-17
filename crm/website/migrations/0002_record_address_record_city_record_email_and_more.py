# Generated by Django 5.0.7 on 2024-07-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='address',
            field=models.CharField(default='Default address', max_length=200),
        ),
        migrations.AddField(
            model_name='record',
            name='city',
            field=models.CharField(default='Default city', max_length=50),
        ),
        migrations.AddField(
            model_name='record',
            name='email',
            field=models.CharField(default='default@example.com', max_length=50),
        ),
        migrations.AddField(
            model_name='record',
            name='first_name',
            field=models.CharField(default='default_f_name', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='last_name',
            field=models.CharField(default='default_l_name', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='phone_no',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='state',
            field=models.CharField(default='default_state', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='zipcode',
            field=models.CharField(default='000000', max_length=50),
            preserve_default=False,
        ),
    ]
