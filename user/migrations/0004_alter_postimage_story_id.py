# Generated by Django 3.2.4 on 2021-06-25 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210625_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='story_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.story'),
        ),
    ]