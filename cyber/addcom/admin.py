from django.contrib import admin
from django.contrib.admin.sites import site
from addcom.models import Addcom
class AddcomAdmin(admin.ModelAdmin):
    list_display=('computer_id','computer_name','company','type','model_no','series','ram')

admin.site.register(Addcom,AddcomAdmin)

# Register your models here.
