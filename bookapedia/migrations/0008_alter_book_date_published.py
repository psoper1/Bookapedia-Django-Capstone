# Generated by Django 4.2 on 2023-04-20 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapedia', '0007_alter_book_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_published',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
