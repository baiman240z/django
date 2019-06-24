# Generated by Django 2.2.2 on 2019-06-23 08:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoSandbox', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hoge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('body', models.CharField(max_length=3000)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Hode',
        ),
    ]
