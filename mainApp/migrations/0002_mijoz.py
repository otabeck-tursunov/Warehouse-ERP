# Generated by Django 5.0.2 on 2024-03-02 14:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mijoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('dokon', models.CharField(blank=True, max_length=255, null=True)),
                ('tel', models.CharField(max_length=14)),
                ('manzil', models.TextField()),
                ('qarz', models.FloatField(default=0)),
                ('tarqatuvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
