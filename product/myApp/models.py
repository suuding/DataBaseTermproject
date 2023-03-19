from django.db import models

# Create your models here.

class Product(models.Model):
    maker = models.CharField(max_length=1, blank=True, null=True)
    model = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'
        
        
class Pc(models.Model):
    model = models.OneToOneField('Product', models.DO_NOTHING, db_column='model', primary_key=True)
    speed = models.FloatField(blank=True, null=True)
    ram = models.IntegerField(blank=True, null=True)
    hd = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
    color = models.CharField(max_length=5, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'printer'
        
        
class Laptop(models.Model):
    model = models.OneToOneField('Product', models.DO_NOTHING, db_column='model', primary_key=True)
    speed = models.FloatField(blank=True, null=True)
    ram = models.IntegerField(blank=True, null=True)
    hd = models.IntegerField(blank=True, null=True)
    screen = models.FloatField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laptop'
        

class Printer(models.Model):
    model = models.OneToOneField('Product', models.DO_NOTHING, db_column='model', primary_key=True)
    color = models.CharField(max_length=5, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'printer'