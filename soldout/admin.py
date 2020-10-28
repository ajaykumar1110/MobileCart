from django.contrib import admin
from .models import Sold

class SoldAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

    def created(self, obj):
        return 'created test'

admin.site.register(Sold, SoldAdmin)