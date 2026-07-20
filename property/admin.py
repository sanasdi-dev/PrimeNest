from django.contrib import admin
from .models import (
    Property,
    PropertyType,
    Agent,
    Amenity,
    PropertyImage,
    VisitRequest
)


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'property')


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'city',
        'price',
        'status',
        'created_at',
    )

    search_fields = (
        'title',
        'city',
    )

    list_filter = (
        'city',
        'status',
        'property_type',
    )

    prepopulated_fields = {
        'slug': ('title',)
    }
@admin.register(VisitRequest)
class VisitRequestAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'property',
        'phone',
        'created_at',
    )

    search_fields = (
        'name',
        'email',
        'phone',
    )

    list_filter = (
        'created_at',
    )