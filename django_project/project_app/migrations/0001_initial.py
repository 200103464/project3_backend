# Generated by Django 4.0.4 on 2022-05-05 16:27

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
