# Generated by Django 4.0.5 on 2022-06-27 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('testapp1', '0002_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bday', models.DateTimeField(verbose_name='birthday')),
            ],
        ),
    ]
