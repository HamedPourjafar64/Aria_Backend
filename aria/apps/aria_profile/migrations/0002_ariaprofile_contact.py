# Generated by Django 3.0.5 on 2021-02-20 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aria_contact', '0003_remove_contact_profile'),
        ('aria_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ariaprofile',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aria_contact.Contact'),
        ),
    ]
