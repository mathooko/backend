# Generated by Django 5.0.1 on 2024-04-28 18:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LaundryService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trousers', models.IntegerField(null=True)),
                ('tshirts', models.IntegerField(null=True)),
                ('sweaters', models.IntegerField(null=True)),
                ('shorts', models.IntegerField(null=True)),
                ('personal', models.IntegerField(null=True)),
                ('duvet', models.IntegerField(null=True)),
                ('shoes', models.IntegerField(null=True)),
                ('iron', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
