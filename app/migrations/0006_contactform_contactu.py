# Generated by Django 4.1.4 on 2022-12-30 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_services_servicesbtn_servicetitle_whatwedo_creative'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourName', models.TextField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('Phonenumber', models.CharField(max_length=20)),
                ('Subject', models.CharField(choices=[('seo', 'SEO'), ('WebDesign', 'WEBDESIGN'), ('SocialMediaMarketing', 'SOCIALMEDIAMARKETING'), ('WebDevelopment', 'WEBDEVELOPMENT'), ('EmailMarketing', 'EMAILMARKETING'), ('ADsManagement', 'ADMANAGEMENT')], max_length=100)),
                ('Message', models.CharField(max_length=400)),
                ('btn', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ContactU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintitle', models.CharField(max_length=30)),
                ('title1', models.CharField(max_length=50)),
                ('title2', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
