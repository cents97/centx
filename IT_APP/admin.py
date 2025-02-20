from django.contrib import admin
from .models import Product, ProductRequest, Project

# Register your models here.



admin.site.register(Product)
admin.site.register(ProductRequest)


admin.site.register(Project)

from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "message")


