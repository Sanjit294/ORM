# Generated by Django 5.2 on 2025-04-17 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('release_year', models.IntegerField()),
                ('genre', models.CharField(max_length=50)),
                ('rating', models.FloatField()),
            ],
        ),
    ]
