# Generated by Django 4.2.10 on 2024-02-17 09:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserIdentity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('token', models.CharField(max_length=255)),
                ('external_id', models.CharField(default='id', max_length=255)),
                ('name', models.CharField(default='unknown', max_length=255)),
                ('username', models.CharField(default='unknown', max_length=255)),
                ('email', models.EmailField(default='unknown', max_length=254)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.identityprovider')),
            ],
            options={
                'verbose_name': 'Identidade do usuario',
                'verbose_name_plural': 'Identidades dos usuarios',
            },
        ),
    ]
