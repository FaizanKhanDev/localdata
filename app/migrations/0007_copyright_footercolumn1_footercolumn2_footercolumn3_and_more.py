# Generated by Django 4.1.4 on 2022-12-31 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_contactform_contactu'),
    ]

    operations = [
        migrations.CreateModel(
            name='CopyRight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FooterColumn1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('item1', models.CharField(max_length=100)),
                ('item2', models.CharField(max_length=100)),
                ('item3', models.CharField(max_length=100)),
                ('item4', models.CharField(max_length=100)),
                ('item5', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FooterColumn2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('item1', models.CharField(max_length=100)),
                ('item2', models.CharField(max_length=100)),
                ('item3', models.CharField(max_length=100)),
                ('item4', models.CharField(max_length=100)),
                ('item5', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FooterColumn3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('item1', models.CharField(max_length=100)),
                ('item2', models.CharField(max_length=100)),
                ('item3', models.CharField(max_length=100)),
                ('item4', models.CharField(max_length=100)),
                ('item5', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FooterColumn4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('item1', models.CharField(max_length=100)),
                ('item2', models.CharField(max_length=100)),
                ('item3', models.CharField(max_length=100)),
                ('item4', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryColumn1image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='allimages')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryColumn2image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='allimages')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryColumn3image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='allimages')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryColumn4image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='allimages')),
            ],
        ),
    ]
