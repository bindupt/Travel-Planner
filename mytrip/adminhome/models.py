from django.db import models

# Create your models here.
class CountryModel(models.Model):
        Country = models.CharField(max_length=20,null=True)
        def __str__(self):
                return self.Country






class StateModel(models.Model):
        country =models.ForeignKey(CountryModel,on_delete=models.CASCADE,default=1)
        State = models.CharField(max_length=20,null=True)
        def __str__(self):
                return self.State
#
#
class DistrictModel(models.Model):
        state =models.ForeignKey(StateModel,on_delete=models.CASCADE,default=1)
        District = models.CharField(max_length=20,null=True)
        Area = models.CharField(max_length=20,null=True)
        Population = models.CharField(max_length=20,null=True)
        Altitude = models.CharField(max_length=20,null=True)
        Telcode = models.CharField(max_length=20,null=True)
        Description = models.TextField(max_length=200)
        Air=models.CharField(max_length=20,null=True)
        Rail=models.CharField(max_length=20,null=True)
        Road=models.CharField(max_length=20,null=True)
        Backwarter=models.CharField(max_length=20,null=True)
        def __str__(self):
                return self.District
#
class LocationModel(models.Model):
        district=models.ForeignKey(DistrictModel,on_delete=models.CASCADE,default=1)
        Location=models.CharField(max_length=20,null=True)
        Description=models.TextField(max_length=200)
        Hw_to_reach=models.CharField(max_length=20,null=True)
        def __str__(self):
                return self.Location
    #create destination category model
class Destination_catModel(models.Model):
        Destination_cat = models.CharField(max_length=20,null=True)
        def __str__(self):
                return self.Destination_cat
#
 #create destination  model
class DestinationModel(models.Model):
        Destination = models.CharField(max_length=20,null=True)
        Category =models.ForeignKey(Destination_catModel,on_delete=models.CASCADE)
        Location =models.ForeignKey(LocationModel,on_delete=models.CASCADE)
        District =models.ForeignKey(DistrictModel,on_delete=models.CASCADE)
        state =models.ForeignKey(StateModel,on_delete=models.CASCADE)
         #create Stay type   model
class Stay_categoryModel(models.Model):
        Stay_type = models.CharField(max_length=20,null=True)
        photo = models.FileField(upload_to="photos", blank=True)
        class Meta:
                db_table = "stay_cat_table"
