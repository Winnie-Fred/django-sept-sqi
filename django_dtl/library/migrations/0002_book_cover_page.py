# Generated by Django 5.1.1 on 2024-09-24 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_page',
            field=models.ImageField(blank=True, null=True, upload_to='book_cover_pages/'),
        ),
    ]
