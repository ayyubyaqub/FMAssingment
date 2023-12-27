from django.db import models

# Create your models here.

# vendors starts from here

def get_vendor_id():
    now = datetime.now()
    code = now.strftime("%y%m%d%H%M")
    today=date.today()
    count = Vendor.objects.filter(created_at__date=today).count()+1
    digit = str(count).zfill(3)   
    vendor_code = "FMV"+str(code)+'A'+str(digit)
    return (vendor_code)

from datetime import date,datetime
class Vendor(models.Model):
    name=models.CharField(max_length=100)
    contact_details=models.TextField()
    address=models.TextField()
    vendor_code=models.CharField(max_length=20,unique=True,editable=False,default=get_vendor_id,)
    on_time_delivery_rate=models.FloatField(default=0)
    quality_rating_avg=models.FloatField(default=0)
    average_response_time=models.FloatField(default=0)
    fulfillment_rate=models.FloatField(default=0)
    created_at=models.DateTimeField(null=True,blank=True,auto_now_add=True)


status=[
    (1,'pending'),
    (2,'completed'),
    (3,'canceled'),
]
def get_po_number():
    now = datetime.now()
    code = now.strftime("%y%m%d%H%M")
    today=date.today()
    print(today)
    count = Purchase_order.objects.filter(order_date__date=today).count()+1
    digit = str(count).zfill(3)   
    po_number = "FMPO"+str(code)+'A'+str(digit)
    return (po_number)

class Purchase_order(models.Model):
    po_number=models.CharField(max_length=20,unique=True,editable=False,default=get_po_number,)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE,related_name='purchase_orders')
    order_date=models.DateTimeField(auto_now_add=True)
    delivery_date=models.DateTimeField(null=True,blank=True)
    items=models.JSONField()
    quantity=models.IntegerField()
    status=models.IntegerField(choices=status,null=True,blank=True,default=1)
    quality_rating=models.FloatField(null=True,blank=True)
    issue_date=models.DateTimeField(auto_now_add=True)
    acknowledgment_date=models.DateTimeField(null=True,blank=True)
    po_delivered_on=models.DateTimeField(null=True,blank=True)


class Vendor_performance_History(models.Model):
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE,related_name='performance_history')
    date=models.DateTimeField()
    on_time_delivery_rate=models.FloatField()
    quality_rating_avg=models.FloatField( )
    average_response_time=models.FloatField()
    fulfillment_rate=models.FloatField()


from django.db.models import F
from django.db.models.signals import pre_save ,post_save
from django.dispatch import receiver



from django.db.models import Avg
@receiver(pre_save,sender=Purchase_order)
def vendor_performance_history(sender,instance,**kwargs):
    if instance.status==2:
        instance.po_delivered_on=datetime.now()
        
from datetime import datetime,timedelta

@receiver(post_save,sender=Purchase_order)
def vendor_performance_history(sender,update_fields,instance,created,**kwargs):
    if not created:
        ontime_delivered_po=Purchase_order.objects.filter(vendor=instance.vendor,po_delivered_on__lte=F('delivery_date'),status=2).count()#here F tells the field name to compare
        total_completed_po=Purchase_order.objects.filter(vendor=instance.vendor,status=2).count()
        on_time_delivery_rate=ontime_delivered_po/total_completed_po 
        quality_rating_avg=Purchase_order.objects.filter(vendor=instance.vendor,status=2).aggregate(Avg("quality_rating", default=0))
    
        average_response_time=Purchase_order.objects.filter(vendor=instance.vendor).aggregate(average_difference=Avg(F('acknowledgment_date') - F('issue_date')))['average_difference'].total_seconds()
        # average response time in seconds
        fulfillment_rate=Purchase_order.objects.filter(vendor=instance.vendor,status=2).count()/Purchase_order.objects.filter(vendor=instance.vendor).count()
        
        Vendor_performance_History.objects.create(vendor=instance.vendor,date=datetime.now(),on_time_delivery_rate=on_time_delivery_rate,quality_rating_avg=quality_rating_avg['quality_rating__avg'],average_response_time=average_response_time,fulfillment_rate=fulfillment_rate)
        Vendor.objects.filter(id=instance.vendor.id).update(on_time_delivery_rate=on_time_delivery_rate,quality_rating_avg=quality_rating_avg['quality_rating__avg'],average_response_time=average_response_time,fulfillment_rate=fulfillment_rate)
   
