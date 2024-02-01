# Generated by Django 5.0.1 on 2024-02-01 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('UserID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=256)),
                ('Email', models.EmailField(max_length=254)),
                ('MembershipDate', models.DateField()),
            ],
        ),
    ]