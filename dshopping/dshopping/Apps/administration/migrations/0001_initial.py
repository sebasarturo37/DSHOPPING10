# Generated by Django 2.2.6 on 2019-10-23 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=150, verbose_name='First name')),
                ('lastname', models.CharField(max_length=150, verbose_name='Last name')),
                ('phone', models.BigIntegerField(verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('password', models.CharField(max_length=150, verbose_name='Password')),
                ('credit_card_number', models.BigIntegerField(verbose_name='Credit card ')),
                ('image', models.ImageField(blank=True, null=True, upload_to='clients/', verbose_name='Author image')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('abbreviation', models.CharField(max_length=150, verbose_name='Abbreviation')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Genders',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('status', models.BooleanField(default=True)),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Category')),
                ('id_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Country')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shopping_date', models.DateTimeField(auto_now_add=True)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Client')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Product')),
            ],
            options={
                'verbose_name': 'Shopping',
                'verbose_name_plural': 'Shoppings',
            },
        ),
        migrations.AddField(
            model_name='client',
            name='id_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Country'),
        ),
        migrations.AddField(
            model_name='client',
            name='id_gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Gender'),
        ),
    ]
