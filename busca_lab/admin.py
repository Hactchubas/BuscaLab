from django.contrib import admin
from .models import PC_model, Software, Lab, Quantity, Report, Equipament



# Register your models here.
class Pc_Model_Admin(admin.ModelAdmin):
    list_display = ("id","manufacturer","name","processor", "cpu_mark","mem_capacity","mem_type","operational_system")

class LabAdmin(admin.ModelAdmin):
    filter_horizontal = ("model","softwares","equipaments")
    list_display = ( "name","id",)


class QuantityAdmin(admin.ModelAdmin):
    list_display = ("model","lab","quantity")
   

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ("id","name","category","version","lisence",)


    


admin.site.register(PC_model, Pc_Model_Admin)
admin.site.register(Software,SoftwareAdmin)
admin.site.register(Lab,LabAdmin)
admin.site.register(Quantity,QuantityAdmin)
admin.site.register(Report)
admin.site.register(Equipament)


# Register your models here.
