from django.contrib import admin
from .models import Stock
from .models import Sold

class StockAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    def created(self, obj):
        return 'created test'

class SoldAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    def created(self, obj):
        return 'created test'


admin.site.register(Stock, StockAdmin)

admin.site.register(Sold, SoldAdmin)