from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField('Title', max_length = 150)
    description = models.TextField('Description')
    status = models.BooleanField(default = True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title

class Country(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField('Title', max_length = 150)
    abbreviation = models.CharField('Abbreviation', max_length = 150)
    status = models.BooleanField(default = True)
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
    def __str__(self):
        return self.title

class Product(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField('Title', max_length = 150)
    description = models.TextField('Description')
    id_category = models.ForeignKey(Category, on_delete = models.CASCADE)
    id_country = models.ForeignKey(Country, on_delete = models.CASCADE)
    quantity = models.IntegerField('Quantity')
    status = models.BooleanField(default = True)
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def __str__(self):
        return self.title

class Gender(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField('Title', max_length = 150)
    description = models.TextField('Description')
    status = models.BooleanField(default = True)
    class Meta:
        verbose_name ='Gender'
        verbose_name_plural ='Genders'
    def __str__(self):
        return self.title

class Client(models.Model):
    id = models.AutoField(primary_key = True)
    firstname = models.CharField('First name', max_length = 150)
    lastname = models.CharField('Last name', max_length = 150)
    id_gender = models.ForeignKey(Gender, on_delete = models.CASCADE)
    phone = models.BigIntegerField('Phone')
    email = models.EmailField('E-mail')
    password = models.CharField('Password',max_length = 150)
    id_country = models.ForeignKey(Country, on_delete = models.CASCADE)
    credit_card_number = models.BigIntegerField('Credit card ')
    image = models.ImageField('Author image', null = True, blank = True, upload_to = 'clients/')
    status = models.BooleanField(default = True)
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    def __str__(self):
        return self.firstname

class Shopping (models.Model):
    id = models.AutoField(primary_key = True)
    id_product = models.ForeignKey(Product,on_delete = models.CASCADE)
    id_client = models.ForeignKey(Client,on_delete = models.CASCADE)
    shopping_date = models.DateTimeField(auto_now_add = True)
    class Meta:
        verbose_name = 'Shopping'
        verbose_name_plural = 'Shoppings'
    def __int__(self):
        return self.id
