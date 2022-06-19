from django.db import models

# Create your models here.


from django.db import models

class MainappOrder(models.Model):
    channel = models.CharField(max_length=2)
    brand = models.CharField(max_length=100, null=True, blank=True)
    fulfillment_partner = models.CharField(max_length=100, null=True, blank=True)
    order_id = models.CharField(max_length=50, null=True, blank=True) # maybe int not str 
    status = models.CharField(max_length=50, null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    total = models.DecimalField (max_digits=10,decimal_places=7, null=True, blank=True) # i need fix this later 
    delivery_zone = models.CharField(max_length=50, null=True, blank=True)
    details = models.CharField(max_length=100, null=True, blank=True)
    customer_name = models.CharField(max_length=100, null=True, blank=True)
    customer_mobile_number =models.IntegerField( null=True, blank=True)

 
    class Meta:
        managed = False
        db_table = 'mainapp_order'
        app_label  = 'scrapper'

