# Generated by Django 5.0.1 on 2024-01-30 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('contact', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
                ('co_pass', models.CharField(max_length=50)),
            ],
        ),
    ]
