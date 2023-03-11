from django.contrib import admin
from .models import Services, AboutUs


class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'nr',
        'name',
        'description',
        'price',
        'image',
    )

    ordering = (
        'nr',
    )


class AboutUsAdmin(admin.ModelAdmin):
    list_display = (
        'nr',
        'title',
        'content',
        'image',
    )

    ordering = (
        'nr',
    )


admin.site.register(Services, ServicesAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
