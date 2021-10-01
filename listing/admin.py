from django.contrib import admin
from .models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    ordering= ('id',)
    list_display= ['id', 'title', 'owner', 'category', 'price', 'is_published', 'list_date']
    list_display_links= ['id', 'title']
    list_filter= ['owner', 'category']
    search_fields= ('title', 'price')
    list_editable= ['is_published',]
    list_per_page= 15


admin.site.register(Listing, ListingAdmin)
