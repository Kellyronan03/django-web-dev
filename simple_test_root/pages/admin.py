from django.contrib import admin

from .models import Page

# Customizes the display and behavior of Page model in Django admin
class PageAdmin(admin.ModelAdmin):
    list_display = ('title','update_date')
    ordering = ('title',)
    search_fields = ('title',)

# Register the Page model with its custom admin configuration
admin.site.register(Page, PageAdmin)
