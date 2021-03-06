# Generated by Django 3.1.7 on 2021-03-21 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aria_address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_deleted', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(1, 'IN_PROGRESS'), (2, 'DONE'), (3, 'CANCELED')], default=1, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('dst_addr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dst_addr', to='aria_address.address')),
                ('service_worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_worker', to=settings.AUTH_USER_MODEL)),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='service', to='service.service')),
                ('src_addr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='src_addr', to='aria_address.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
