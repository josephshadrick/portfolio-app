# Generated by Django 5.1.6 on 2025-02-19 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('date', models.TextField()),
                ('img', models.ImageField(upload_to='')),
                ('github', models.TextField(blank=True, null=True)),
                ('website', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('category', models.TextField()),
                ('years', models.IntegerField()),
            ],
        ),
    ]
