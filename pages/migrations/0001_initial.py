# Generated by Django 4.2 on 2023-04-11 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=600)),
                ('image', models.FileField(blank=True, null=True, upload_to='covers/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wanted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=15)),
                ('origin', models.CharField(max_length=10)),
                ('image', models.FileField(upload_to='covers/')),
                ('reward', models.IntegerField(null=True)),
            ],
        ),
    ]
