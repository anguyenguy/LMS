# Generated by Django 2.2.14 on 2020-07-09 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_sequences', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesectionsequence',
            name='inaccessible_after_due',
            field=models.BooleanField(default=False),
        ),
    ]
