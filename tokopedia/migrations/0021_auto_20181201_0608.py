# Generated by Django 2.1.2 on 2018-11-30 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokopedia', '0020_good_barang_dilihat_int'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='toko_url_full',
            field=models.URLField(default='www.google.com'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='good',
            name='barang_kondisi',
            field=models.IntegerField(blank=True, choices=[(1, 'Baru'), (2, '2?'), (3, '3?'), (4, '4?'), (5, '5?')], null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='toko_follower_int',
            field=models.CharField(blank=True, default=0, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='toko_is_gold',
            field=models.BooleanField(default=False, verbose_name='Gold Merchant'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='toko_is_official',
            field=models.BooleanField(default=False, verbose_name='Toko Official'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='toko_jumlah_barang',
            field=models.IntegerField(blank=True, null=True, verbose_name='Jumlah Barang'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='toko_kota',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Kota Toko'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='toko_lokasi',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Lokasi Toko'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='toko_reputasi_level',
            field=models.IntegerField(blank=True, choices=[(20, 'Diamond 5'), (19, 'Diamond 4'), (18, 'Diamond 3'), (17, 'Diamond 2'), (16, 'Diamond 1'), (15, 'Gold 5'), (14, 'Gold 4'), (13, 'Gold 3'), (12, 'Gold 2'), (11, 'Gold 1'), (10, 'Silver 5'), (9, 'Silver 4'), (8, 'Silver 3'), (7, 'Silver 2'), (6, 'Silver 1'), (5, 'Bronze 5'), (4, 'Bronze 4'), (3, 'Bronze 3'), (2, 'Bronze 2'), (1, 'Bronze 1'), (0, 'Belum ada reputasi')], null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='toko_terjual_int',
            field=models.CharField(blank=True, default=0, max_length=50, null=True),
        ),
    ]
