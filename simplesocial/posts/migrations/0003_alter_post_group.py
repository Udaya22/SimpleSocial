# Generated by Django 4.0.6 on 2022-09-07 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_initial'),
        ('posts', '0002_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='groups.group'),
            preserve_default=False,
        ),
    ]
