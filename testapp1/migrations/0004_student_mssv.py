# Generated by Django 4.0.5 on 2022-06-27 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp1', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mssv',
            field=models.BigIntegerField(default=2183143, verbose_name=50),
            preserve_default=False,
        ),
    ]
