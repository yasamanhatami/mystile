# Generated by Django 5.0.4 on 2024-06-21 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_post_id_post_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='number',
        ),
        migrations.AddField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]