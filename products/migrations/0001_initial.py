# Generated by Django 4.0.4 on 2022-05-20 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoper_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('shoper_ean', models.CharField(blank=True, max_length=13)),
                ('shoper_sku', models.CharField(blank=True, max_length=25, unique=True)),
                ('shoper_weight', models.CharField(blank=True, max_length=100)),
                ('is_active_shoper', models.BooleanField(blank=True, null=True)),
                ('vendor_brand', models.CharField(blank=True, max_length=100)),
                ('created_shoper', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_shoper', models.CharField(blank=True, max_length=50, null=True)),
                ('shoper_price', models.CharField(blank=True, max_length=40)),
                ('shoper_gauge_id', models.CharField(blank=True, max_length=20, null=True)),
                ('shoper_discount_value', models.CharField(blank=True, max_length=10)),
                ('shoper_promo_id', models.IntegerField(blank=True, null=True)),
                ('shoper_promo_start', models.CharField(blank=True, max_length=50, null=True)),
                ('shoper_promo_ends', models.CharField(blank=True, max_length=50, null=True)),
                ('shoper_bestseller_tag', models.BooleanField(blank=True, null=True)),
                ('shoper_new_product_tag', models.BooleanField(blank=True, null=True)),
                ('shoper_promo_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('shoper_tags', models.CharField(blank=True, max_length=200)),
                ('shoper_title_pl', models.CharField(max_length=200)),
                ('shoper_title_en', models.CharField(blank=True, max_length=200)),
                ('shoper_title_fr', models.CharField(blank=True, max_length=200)),
                ('shoper_title_de', models.CharField(blank=True, max_length=200)),
                ('shoper_description_pl', models.TextField(blank=True)),
                ('shoper_seo_title_pl', models.CharField(blank=True, max_length=200)),
                ('shoper_meta_desc_pl', models.TextField(blank=True)),
                ('shoper_permalink_pl', models.CharField(blank=True, max_length=200)),
                ('shoper_seo_url_pl', models.CharField(blank=True, max_length=200)),
                ('shoper_description_en', models.TextField(blank=True)),
                ('shoper_seo_title_en', models.CharField(blank=True, max_length=200)),
                ('shoper_meta_desc_en', models.TextField(blank=True)),
                ('shoper_permalink_en', models.CharField(blank=True, max_length=200)),
                ('shoper_seo_url_en', models.CharField(blank=True, max_length=200)),
                ('shoper_description_fr', models.TextField(blank=True)),
                ('shoper_seo_title_fr', models.CharField(blank=True, max_length=200)),
                ('shoper_meta_desc_fr', models.TextField(blank=True)),
                ('shoper_permalink_fr', models.CharField(blank=True, max_length=200)),
                ('shoper_seo_url_fr', models.CharField(blank=True, max_length=200)),
                ('shoper_description_de', models.TextField(blank=True)),
                ('shoper_seo_title_de', models.CharField(blank=True, max_length=200)),
                ('shoper_meta_desc_de', models.TextField(blank=True)),
                ('shoper_permalink_de', models.CharField(blank=True, max_length=200)),
                ('shoper_seo_url_de', models.CharField(blank=True, max_length=200)),
                ('shopify_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('shopify_ean', models.CharField(blank=True, max_length=13)),
                ('shopify_sku', models.CharField(blank=True, max_length=25)),
                ('shopify_title', models.CharField(blank=True, max_length=200, null=True)),
                ('shopify_description', models.TextField(blank=True, null=True)),
                ('shopify_position', models.CharField(blank=True, max_length=20)),
                ('is_active_shopify', models.CharField(blank=True, max_length=1)),
                ('shopify_tags', models.CharField(blank=True, max_length=200)),
                ('created_shopify', models.DateTimeField(blank=True, null=True)),
                ('updated_shopify', models.DateTimeField(blank=True, null=True)),
                ('shopify_price', models.CharField(blank=True, max_length=40)),
                ('shopify_seo_title', models.CharField(blank=True, max_length=200)),
                ('shopify_seo_description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('shoper_images', models.ManyToManyField(blank=True, to='images.image')),
            ],
        ),
    ]
