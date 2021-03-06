# Generated by Django 3.1.7 on 2021-03-21 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aria_address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=32)),
                ('tag_name', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fax_number', models.CharField(max_length=32, null=True)),
                ('name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=128)),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='aria_address.address')),
                ('phone_numbers', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aria_contact.phonenumber')),
            ],
        ),
    ]
