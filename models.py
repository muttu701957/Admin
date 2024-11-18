from django.db import models

# Create your models here.

class Purchagemaster(models.Model):
    bill_no=models.CharField(max_length=200, null=True)
    purchage_date=models.CharField(max_length=200, null=True)
    customer_name=models.CharField(max_length=200, null=True)
    item=models.CharField(max_length=200, null=True)
    unit_text=models.CharField(max_length=200, null=True)
    gst=models.CharField(max_length=200, null=True)
    qty=models.IntegerField(blank=True, null=True)
    total_price=models.IntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.customer_name

class addpureMaster(models.Model):
    item=models.CharField(max_length=200, null=True)
    price=models.IntegerField(blank=True, null=True)

class customer(models.Model):
    farmer_name=models.CharField(max_length=200, null=True)
    address=models.CharField(max_length=200, null=True)
    mobile_num=models.IntegerField(blank=True, null=True)
    packet_no=models.IntegerField(blank=True, null=True)
    packet_name=models.CharField(max_length=200, null=True)

class Nurserymaster(models.Model):
    bill_no=models.CharField(max_length=200, null=True)
    farmer_name=models.CharField(max_length=200, null=True)
    description=models.CharField(max_length=200, null=True)
    advance=models.CharField(max_length=200, null=True)
    total_price=models.IntegerField(blank=True, null=True)
    price=models.IntegerField(blank=True, null=True)
    address=models.CharField(max_length=200, null=True)
    tray_no=models.IntegerField(blank=True, null=True)
    nursery_date=models.CharField(max_length=200, null=True)
    swoing_date=models.CharField(max_length=200, null=True)
    lot_no=models.IntegerField(blank=True, null=True)
    mobile_num=models.IntegerField(blank=True, null=True)
    packet_no=models.IntegerField(blank=True, null=True)
    packet_name=models.CharField(max_length=200, null=True)

class PartylistMaster(models.Model):
    bill_no=models.CharField(max_length=200, null=True)
    customer_name=models.CharField(max_length=200, null=True)
    date=models.CharField(max_length=200, null=True)
    address=models.CharField(max_length=200, null=True)
    mobile_num=models.IntegerField(blank=True, null=True)

class PartylistdeleteMaster(models.Model):
    bill_no=models.CharField(max_length=200, null=True)
    farmer_name=models.CharField(max_length=200, null=True)
    seed_name=models.CharField(max_length=200, null=True)
    address=models.CharField(max_length=200, null=True)
    qty=models.IntegerField(blank=True, null=True)
    price=models.IntegerField(blank=True, null=True)
    advn=models.IntegerField(blank=True, null=True)
    tprice=models.IntegerField(blank=True, null=True)
    seed_date=models.CharField(max_length=200, null=True)

class PBcustomerMaster(models.Model):
    customer_name=models.CharField(max_length=200, null=True)
    address=models.CharField(max_length=200, null=True)
    mobile_num=models.IntegerField(blank=True, null=True)

class PbsugarcaneMaster(models.Model):
    bill_no=models.CharField(max_length=200, null=True)
    farmer_name=models.CharField(max_length=200, null=True)
    nursery_date=models.CharField(max_length=200, null=True)
    address=models.CharField(max_length=200, null=True)
    mobile_num=models.IntegerField(blank=True, null=True)
    item=models.CharField(max_length=200, null=True)
    verity_no=models.CharField(max_length=200, null=True)
    vehicle_no=models.CharField(max_length=200, null=True)
    weibrage_weight=models.IntegerField(blank=True, null=True)
    vehicle_weight=models.IntegerField(blank=True, null=True)
    price=models.IntegerField(blank=True, null=True)
    advance=models.IntegerField(blank=True, null=True)
    total_price=models.IntegerField(blank=True, null=True)

class SBcustomerMaster(models.Model):
    customer_name=models.CharField(max_length=200, null=True)
    address=models.CharField(max_length=200, null=True)
    mobile_num=models.IntegerField(blank=True, null=True)

class SbsugarMaster(models.Model):
    description=models.CharField(max_length=200,null=True)
    bill_no=models.CharField(max_length=200, null=True)
    farmer_name=models.CharField(max_length=200, null=True)
    nursery_date=models.CharField(max_length=200, null=True)
    address=models.CharField(max_length=200, null=True)
    mobile_num=models.IntegerField(blank=True, null=True)
    verity_no=models.CharField(max_length=200, null=True)
    seedlings_no=models.CharField(max_length=200, null=True)
    price=models.IntegerField(blank=True, null=True)
    advance=models.IntegerField(blank=True, null=True)
    total_price=models.IntegerField(blank=True, null=True)

class LabourMaster(models.Model):
    farmer_name=models.CharField(max_length=200, null=True)
    address=models.CharField(max_length=200, null=True)
    mobile_num=models.IntegerField(blank=True, null=True)

class sclabourMaster(models.Model):
    bill_no=models.CharField(max_length=200, null=True)
    labour_name=models.CharField(max_length=200, null=True)
    address=models.CharField(max_length=200, null=True)
    mobile_num=models.IntegerField(blank=True, null=True)
    description=models.CharField(max_length=200,null=True)
    vehicle_no=models.CharField(max_length=200, null=True)
    cane_weight=models.IntegerField(blank=True, null=True)
    price=models.IntegerField(blank=True, null=True)
    total_price=models.IntegerField(blank=True, null=True)

class incustMaster(models.Model):
    farmer_name=models.CharField(max_length=200, null=True)
    factory=models.CharField(max_length=200, null=True)
    address=models.CharField(max_length=200, null=True)
    mobile_num=models.IntegerField(blank=True, null=True)

class inlistMaster(models.Model):
    bill_no=models.IntegerField(blank=True, null=True)
    factory=models.CharField(max_length=200, null=True)
    address=models.CharField(max_length=200, null=True)
    mobile_num=models.IntegerField(blank=True, null=True)
    place=models.CharField(max_length=200, null=True)
    circle=models.CharField(max_length=200, null=True)
    field_name=models.CharField(max_length=200, null=True)
    field_num=models.IntegerField(blank=True, null=True)
    farmer=models.CharField(max_length=200, null=True)
    description=models.CharField(max_length=200, null=True)
    indent_no=models.CharField(max_length=200, null=True)
    verity_code=models.CharField(max_length=200, null=True)
    seedlings_no=models.CharField(max_length=200, null=True)
    price=models.IntegerField(blank=True, null=True)
    total_price=models.IntegerField(blank=True, null=True)