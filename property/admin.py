from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': (
                'town', 'town_district', 'address', 'owner', 'owners_phonenumber',
                'price', 'rooms_number', 'living_area', 'floor', 'has_balcony',
                'description', 'construction_year', 'active', 'new_building', 'likes'
            )
        }),
        ('Дата создания', {
            'fields': ('created_at',),
        }),
    )
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'owner', 'active')
    list_editable = ('new_building',)
    list_filter = ('town', 'rooms_number', 'active', 'new_building', 'has_balcony', 'construction_year')
    raw_id_fields = ('likes',)


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'created_at')
    raw_id_fields = ('flat', 'user')
    search_fields = ('user__username', 'flat__address', 'text')
    readonly_fields = ('created_at',)
    list_filter = ('flat', 'created_at')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)