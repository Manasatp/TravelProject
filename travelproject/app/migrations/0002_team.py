# Generated by Django 4.2.7 on 2023-11-07 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=100)),
                ('timg', models.ImageField(upload_to='pics')),
                ('tdesc', models.TextField()),
            ],
        ),
    ]
