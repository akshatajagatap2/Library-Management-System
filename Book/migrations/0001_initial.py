# Generated by Django 4.1.1 on 2022-09-09 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200, null=True)),
                ('author_name', models.CharField(max_length=200, null=True)),
                ('publication', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
