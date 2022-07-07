# Generated by Django 4.0.5 on 2022-07-06 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('images', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locale', models.CharField(max_length=20)),
                ('shoper_translation_id', models.IntegerField(unique=True)),
                ('related_product_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('short_description', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('active', models.IntegerField(blank=True, null=True)),
                ('is_default', models.IntegerField(blank=True, null=True)),
                ('lang_id', models.IntegerField(blank=True, null=True)),
                ('seo_title', models.CharField(blank=True, max_length=255)),
                ('seo_description', models.TextField(blank=True)),
                ('seo_keywords', models.TextField(blank=True)),
                ('seo_url', models.CharField(blank=True, max_length=255)),
                ('permalink', models.CharField(max_length=255, unique=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('main_page', models.IntegerField(blank=True, null=True)),
                ('main_page_order', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('shoper_related_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locale', models.CharField(max_length=20)),
                ('shoper_translation_id', models.IntegerField(unique=True)),
                ('related_gfx_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('lang_id', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('shoper_related_gfx', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='images.image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locale', models.CharField(max_length=20)),
                ('shoper_translation_id', models.IntegerField(unique=True)),
                ('related_category_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('description_bottom', models.TextField(blank=True)),
                ('seo_title', models.CharField(blank=True, max_length=255)),
                ('seo_description', models.TextField(blank=True)),
                ('seo_keywords', models.TextField(blank=True)),
                ('seo_url', models.CharField(blank=True, max_length=255)),
                ('permalink', models.CharField(max_length=255, unique=True)),
                ('active', models.IntegerField(blank=True, null=True)),
                ('is_default', models.IntegerField(blank=True, null=True)),
                ('lang_id', models.IntegerField(blank=True, null=True)),
                ('items', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('shoper_related_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
