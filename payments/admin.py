from django.contrib import admin
from .models import Bill

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('title',)
