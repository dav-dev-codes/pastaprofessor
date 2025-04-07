# Generated by Django 5.2 on 2025-04-07 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id_pessoa', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=100)),
                ('telefone', models.TextField(max_length=14)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
    ]
