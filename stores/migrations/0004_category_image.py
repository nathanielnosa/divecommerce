# Generated by Django 4.1.7 on 2023-03-28 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_alter_category_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='category'),
        ),
    ]
