# Generated by Django 2.1.2 on 2018-11-30 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokopedia', '0005_showcase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='reputasi',
        ),
        migrations.AddField(
            model_name='shop',
            name='reputasi_badge',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='reputasi_level',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='reputasi_score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
