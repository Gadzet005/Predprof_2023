from django.contrib import admin

from catalog.models import Site


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    fields = ('name', 'url', 'is_on_catalog', 'logo', 'description')
    ordering = ('is_on_catalog', 'name')
    list_display = ('name', 'url', 'is_on_catalog')
    list_display_links = ('name',)
    list_editable = ('is_on_catalog',)
