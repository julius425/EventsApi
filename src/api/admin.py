from django.contrib import admin
from .models import Event, Transaction


# admin.site.register(Event)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'event_city', 'reserves', 'price')
    list_filter = ('id', 'title', 'date', 'event_city', 'reserves', 'price')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date', 'event', 'transaction_id')
    list_filter = ('amount', 'date', 'event', 'transaction_id')

