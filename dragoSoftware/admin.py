from django.contrib import admin
from .models import Services


class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'image',
    )

    ordering = (
        'name',
    )


admin.site.register(Services, ServicesAdmin)