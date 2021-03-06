# Generated by Django 3.2.12 on 2022-04-06 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecgwebsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('ege', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('F', 'F'), ('M', 'M')], max_length=100, null=True)),
                ('note', models.TextField()),
                ('create_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
