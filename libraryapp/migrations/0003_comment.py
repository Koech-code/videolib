# Generated by Django 4.1.1 on 2022-09-17 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0002_video_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usercomment', models.CharField(max_length=275, null=True)),
            ],
        ),
    ]
