from django.contrib import admin
from cbvapp.models import School,Student



class SchoolAdmin(admin.ModelAdmin):
    
    list_filter=["place",]


# Register your models here
admin.site.register(School)
admin.site.register(Student)
