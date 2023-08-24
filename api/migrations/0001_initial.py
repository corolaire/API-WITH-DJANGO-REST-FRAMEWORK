# Generated by Django 4.2.4 on 2023-08-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullanem', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=50)),
                ('age', models.SmallIntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
