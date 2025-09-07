from django.contrib import admin
from .models import Stocks

@admin.register(Stocks)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_at',)
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = '-id',