from rest_framework import serializers
from .models import Event, Transaction


class EventSerializer(serializers.ModelSerializer):

    """
    Сериалайзер мероприятий
    """

    class Meta:
        model = Event
        fields = ['id', 'title', 'reserves', 'date', 'event_city', 'price', 'description']


class TransactionSerializer(serializers.ModelSerializer):

    """
    Сериалайзер транзакций
    """

    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'date', 'event', 'transaction_id']












