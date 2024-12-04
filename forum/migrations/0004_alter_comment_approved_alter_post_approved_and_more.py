# Generated by Django 4.2.16 on 2024-12-04 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_profile_tagline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tagline',
            field=models.CharField(max_length=200),
        ),
    ]
