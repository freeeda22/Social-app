# Generated by Django 3.2.4 on 2021-06-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_postimage_story_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='story_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]