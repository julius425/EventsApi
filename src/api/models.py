import datetime
from django.db import models
from django.utils import timezone
from django.db import transaction
from django.core.exceptions import ValidationError


def validate_weekend(value):
    if value.weekday() > 4:
        return True


class Event(models.Model):

    """
    Мероприятие
    """

    # TODO:
    SCHEDULE_TYPE = (
        ('daily', 'daily'),
        ('weekly', 'weekly'),
        ('monthly', 'monthly'),
        ('annual', 'annual'),
    )

    PRICES = {
        'weekday': 3000,
        'weekend': 6000,
    }

    title = models.CharField(max_length=100)
    reserves = models.IntegerField()
    event_city = models.CharField(max_length=100)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    description = models.TextField(blank=True)
    # customers = models.ManyToManyField(Customer, related_name='customers', blank=True)
    weekend = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        """
        Перегружаем сэйв для установки ценника мероприятия
        """
        weekend = validate_weekend(self.date)
        if weekend:
            self.price = self.PRICES.get('weekend')
        else:
            self.price = self.PRICES.get('weekday')
        super().save(*args, **kwargs)

    @classmethod
    def get_upcoming(cls):
        """
        Запрос списка ближайших мероприятий
        """
        now = timezone.now()
        upcoming = cls.objects.filter(date__gte=now).exclude(reserves__iexact=0)\
                                                    .order_by('date').order_by('event_city')
        return upcoming

    @classmethod
    def get_event_month_schedule(cls, event_title):
        """
        Запрос расписания конкретного мероприятия на месяц
        """
        today = datetime.date.today()
        month_schedule = cls.objects.filter(title__iexact=event_title,
                                            date__month=today.month)
        return month_schedule


class Transaction(models.Model):

    """
    Транзакция резервирования
    """

    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=50)

    def make_reserve(self):
        """
        Резервируем место, добавляем клиента (покупка билета)
        """
        if self.event.reserves < self.amount:
            raise(ValueError('Нет достаточного количества свободных мест'))

        with transaction.atomic():
            event = self.event
            event.reserves -= self.amount
            event.save()



