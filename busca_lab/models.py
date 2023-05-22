from django.db import models


# Create your models here.

class PC_model(models.Model):
    manufacturer = models.CharField(max_length=64) 
    name = models.CharField(max_length=64)
    processor = models.CharField(max_length=255)
    cpu_mark = models.IntegerField()
    mem_capacity = models.CharField(max_length=6)
    mem_type = models.CharField(max_length=64)
    operational_system = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.manufacturer}: {self.name} | {self.mem_capacity} | {self.operational_system}"

class Software(models.Model):
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    lisence = models.CharField(max_length=64)
    version = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}, version: {self.version}"


class Lab(models.Model):
    name = models.CharField(max_length=64)
    softwares = models.ManyToManyField(Software, blank=True, related_name="installed_in")
    model = models.ManyToManyField(PC_model,blank=True, related_name="locals")
    

    def __str__(self):
        return f"{self.name}" 
    
class Quantity(models.Model):
    model = models.ForeignKey(PC_model, on_delete=models.CASCADE, related_name = "models")
    lab = models.ForeignKey(Lab,on_delete=models.CASCADE, related_name="labs")
    quantity = models.IntegerField()


    def __str__(self):
        return f"{self.model} in {self.lab}, quantity: {self.quantity}"
    class Meta: # new
        
        ordering = ["-lab"]
        






