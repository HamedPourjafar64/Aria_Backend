# Generated by Django 3.1.3 on 2021-02-15 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('serviceCategory', '0001_initial'),
        ('part', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/services/%Y/%m/%d/')),
                ('price', models.BigIntegerField()),
                ('in_place', models.BooleanField(default=False)),
                ('is_transfer', models.BooleanField(default=False)),
                ('service_worker_fee', models.BigIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceCategory.servicecategory')),
                ('parts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='part.part')),
            ],
        ),
    ]
