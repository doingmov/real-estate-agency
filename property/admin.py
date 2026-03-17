from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owners.through
    extra = 0
    verbose_name = "Собственник"
    verbose_name_plural = "Собственники"


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owners__name')
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': (
                'town', 'town_district', 'address', 
                'price', 'rooms_number', 'living_area', 'floor', 'has_balcony',
                'description', 'construction_year', 'active', 'new_building', 'likes'
            )
        }),
        ('Дата создания', {
            'fields': ('created_at',),
        }),
    )
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'active')
    list_editable = ('new_building',)
    list_filter = ('town', 'rooms_number', 'active', 'new_building', 'has_balcony', 'construction_year')
    raw_id_fields = ('likes',)
    inlines = [OwnerInline]


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('author', 'flat', 'created_at')
    raw_id_fields = ('flat', 'author')
    search_fields = ('author__username', 'flat__address', 'text')
    readonly_fields = ('created_at',)
    list_filter = ('flat', 'created_at')


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'phone_pure')
    raw_id_fields = ('flats',)
    search_fields = ('name', 'phone', 'phone_pure')


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)