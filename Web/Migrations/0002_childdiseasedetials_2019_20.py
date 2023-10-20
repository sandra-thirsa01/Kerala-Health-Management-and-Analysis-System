# Generated by Django 4.0.4 on 2022-06-25 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='childdiseasedetials_2019_20',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('District', models.CharField(max_length=20)),
                ('Year', models.CharField(max_length=20)),
                ('pneumonia', models.IntegerField()),
                ('astma', models.IntegerField()),
                ('sephesis', models.IntegerField()),
                ('tetanus', models.IntegerField()),
                ('tuberculosis', models.IntegerField()),
            ],
        ),
    ]