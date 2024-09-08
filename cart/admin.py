from django.contrib import admin
from .models import Order, Item


class AdminOrder(admin.ModelAdmin):
    list_display = ('id', 'date', 'user', 'total', )
    ordering = ('id', 'date', 'user', 'total', )


class AdminItem(admin.ModelAdmin):
    list_display = ('id', 'order', 'order__id', 'movie', 'quantity', 'price')
    list_filter = ('order__id', )
    search_fields = ('order__id', )

admin.site.register(Order, AdminOrder)
admin.site.register(Item, AdminItem)
