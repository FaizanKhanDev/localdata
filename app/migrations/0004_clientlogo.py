# Generated by Django 4.1.4 on 2022-12-29 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_lastestpicture_latesttitle_delete_latest'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='allimages')),
            ],
        ),
    ]