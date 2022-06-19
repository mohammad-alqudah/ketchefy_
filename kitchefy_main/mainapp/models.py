from django.db import models
from django.contrib.auth.models import User

# # ,related_name=
# class kitchefy_user(models.Model):
#     postion = models.CharField(max_length=40)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='kitchefy_user')

#     def __str__(self):
#         return self.user.first_name

# class fp(models.Model):
#     name = models.CharField(max_length=100)
#     user =  models.OneToOneField(User, on_delete=models.CASCADE, related_name='fp_user')

class order(models.Model):
    channel_choices = (
        ('c', 'careem'),
        ('t', 'talabat'),
        ('cs', 'csmena'),
        ('sk', 'ask paper')
    )
    channel  = models.CharField(max_length=2, choices=channel_choices, null=True, blank=True)
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


# class Knowleddge_center_section(models.Model()):
#     name = models.CharField(max_length=50, null=True, blank=True)

# class knowledge_center(models.Model):
#     name =  models.CharField(max_length=50, null=True, blank=True)
#     link =  models.URLField()(max_length=200, null=True, blank=True)
#     image = 
#     video_link  =  models.URLField()(max_length=200, null=True, blank=True)
#     description =  models.CharField(max_length=1000, null=True, blank=True)
#     knowledge_center_section = models.ForeignKey(Knowleddge_center_section, on_delete=models.CASCADE)
#     fp = models.ForeignKey(Knowleddge_center_section, on_delete=models.CASCADE)

    





