# Generated by Django 4.0.3 on 2022-03-23 21:07

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
                ('shoper_title_pl', models.CharField(max_length=200)),
                ('shoper_title_en', models.CharField(blank=True, max_length=200)),
                ('shoper_title_fr', models.CharField(blank=True, max_length=200)),
                ('shoper_title_de', models.CharField(blank=True, max_length=200)),
                ('shoper_description_pl', models.TextField(blank=True)),
                ('shoper_description_en', models.TextField(blank=True)),
                ('shoper_description_fr', models.TextField(blank=True)),
                ('shoper_description_de', models.TextField(blank=True)),
                ('shopify_title', models.CharField(blank=True, max_length=200, null=True)),
                ('shopify_description', models.TextField(blank=True, null=True)),
                ('vendor_brand', models.CharField(blank=True, max_length=100)),
                ('shoper_id', models.IntegerField(unique=True)),
                ('shopify_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('shoper_ean', models.CharField(blank=True, max_length=13)),
                ('shoper_sku', models.CharField(blank=True, max_length=25, unique=True)),
                ('shopify_ean', models.CharField(blank=True, max_length=13)),
                ('shopify_sku', models.CharField(blank=True, max_length=25)),
                ('shopify_position', models.IntegerField(blank=True, null=True)),
                ('shoper_weight', models.CharField(blank=True, max_length=100)),
                ('is_active_shoper', models.BooleanField(default=False)),
                ('is_active_shopify', models.BooleanField(default=False)),
                ('shoper_tags', models.CharField(blank=True, max_length=200)),
                ('shopify_tags', models.CharField(blank=True, max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_shoper', models.DateTimeField(blank=True, null=True)),
                ('updated_shoper', models.DateTimeField(blank=True, null=True)),
                ('created_shopify', models.DateTimeField(blank=True, null=True)),
                ('updated_shopify', models.DateTimeField(blank=True, null=True)),
                ('shoper_price', models.CharField(blank=True, max_length=40)),
                ('shopify_price', models.CharField(blank=True, max_length=40)),
                ('shoper_gauge_id', models.IntegerField(blank=True, null=True)),
                ('shopify_seo_title', models.CharField(blank=True, max_length=200)),
                ('shopify_seo_description', models.TextField(blank=True)),
                ('is_on_shoper', models.BooleanField(default=False)),
                ('is_on_shopify', models.BooleanField(default=False)),
                ('images', models.ManyToManyField(blank=True, to='images.image')),
            ],
        ),
    ]
