# Generated by Django 5.0.6 on 2024-05-13 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('review', models.TextField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos')),
            ],
        ),
    ]
