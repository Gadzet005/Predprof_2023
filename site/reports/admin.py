from django.contrib import admin

from reports.models import SiteReport


@admin.register(SiteReport)
class SiteReportAdmin(admin.ModelAdmin):
    fields = ('is_checked', 'user', 'site', 'region', 'problem', 'creation_datetime')
    readonly_fields = ('user', 'site', 'region', 'problem', 'creation_datetime')
    list_display = ('user', 'site', 'region', 'creation_datetime', 'is_checked')
    list_display_links = ('user',)
    list_filter = ('is_checked', 'creation_datetime')
    list_editable = ('is_checked',)
