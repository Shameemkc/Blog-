# Generated by Django 5.0.6 on 2024-07-20 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('title', models.CharField(default='', max_length=100)),
                ('short_desc', models.CharField(default='', max_length=200)),
                ('content', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='blogimages')),
                ('created_at', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
