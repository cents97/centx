from django.contrib import admin
from .models import Product, ProductRequest, Project, Service, ContactMessage, Testimonial, TeamMember,Category, YouTubeVideo,FAQ

# Register your models here.



admin.site.register(Product)
admin.site.register(ProductRequest)


admin.site.register(Project)

admin.site.register(Service)

admin.site.register(Testimonial)
admin.site.register(TeamMember)

admin.site.register(Category)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "message")


class YouTubeVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url')
    search_fields = ('title',)

admin.site.register(YouTubeVideo, YouTubeVideoAdmin)
admin.site.register(FAQ)



