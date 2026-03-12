from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': (
                'town', 'town_district', 'address', 'owner', 'owners_phonenumber',
                'price', 'rooms_number', 'living_area', 'floor', 'has_balcony',
                'description', 'construction_year', 'active', 'new_building'
            )
        }),
        ('Дата создания', {
            'fields': ('created_at',),
        }),
    )
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('town', 'rooms_number', 'active', 'new_building')


admin.site.register(Flat, FlatAdmin)