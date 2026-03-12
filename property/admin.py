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
                'description', 'construction_year', 'active'
            )
        }),
        ('Дата создания', {
            'fields': ('created_at',),
        }),
    )


admin.site.register(Flat, FlatAdmin)