# Generated by Django 5.0.6 on 2024-06-05 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_user_id_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='RMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('director', models.TextField()),
                ('starring', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
    ]
