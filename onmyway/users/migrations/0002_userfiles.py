# Generated by Django 4.2.11 on 2024-03-16 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('govtid', models.FileField(null=True, upload_to='govtid')),
                ('license', models.FileField(null=True, upload_to='license')),
                ('vehiclecertificate', models.FileField(null=True, upload_to='vehiclecertificate')),
                ('userfile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userfiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
