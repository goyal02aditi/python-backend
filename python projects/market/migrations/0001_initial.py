# Generated by Django 4.2.7 on 2023-11-30 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='When this instance was created.')),
                ('modified', models.DateTimeField(auto_now=True, help_text='When this instance was modified.')),
                ('product_name', models.CharField(max_length=150, verbose_name='product name')),
                ('product_image', models.ImageField(upload_to='product/image/', verbose_name='product image')),
                ('price', models.FloatField(max_length=100, verbose_name='product price')),
                ('category', models.CharField(blank=True, choices=[('indoor', 'Indoor'), ('outdoor', 'Outdoor')], default=None, max_length=55, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
