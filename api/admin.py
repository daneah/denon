from django.contrib import admin

from api import models


@admin.register(models.Command)
class CommandAdmin(admin.ModelAdmin):
    fields = [
        'denon_code',
        'readable_name',
        'description',
        'queryable',
        'icon_code',
    ]

    list_display = [
        'id',
        'denon_code',
        'readable_name',
        'description',
        'queryable',
        'icon_code',
    ]

    list_editable = [
        'denon_code',
        'readable_name',
        'description',
        'queryable',
        'icon_code',
    ]

    sortable_by = [
        'denon_code',
        'readable_name',
        'queryable',
    ]


@admin.register(models.Parameter)
class ParameterAdmin(admin.ModelAdmin):
    fields = [
        'command',
        'denon_code',
        'readable_name',
        'description',
        'icon_code',
    ]

    list_display = [
        'id',
        'command',
        'denon_code',
        'readable_name',
        'description',
        'icon_code',
    ]

    list_editable = [
        'command',
        'denon_code',
        'readable_name',
        'description',
        'icon_code',
    ]

    sortable_by = [
        'command',
        'denon_code',
        'readable_name',
        'icon_code',
    ]
