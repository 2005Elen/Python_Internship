# Generated by Django 5.0.4 on 2024-04-23 18:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0003_alter_user_options_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='created_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_verified', models.BooleanField()),
                ('position', models.CharField(blank=True, max_length=30, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facebook.user')),
            ],
        ),
    ]