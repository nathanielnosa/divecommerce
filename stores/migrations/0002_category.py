# Generated by Django 4.1.7 on 2023-03-28 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Accessories', 'Accessories'), ('Stationeries', 'Stationeries'), ('Electronics', 'Electronics')], max_length=225)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]