from django.test import TestCase
from .models import Event, Transaction
from datetime import datetime
from django.db.models import QuerySet


class AuthorModelTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        weekend_date = datetime.strptime('2019-12-29', '%Y-%m-%d')
        Event.objects.create(title='TestEvent',
                             reserves=100,
                             event_city='Moscow',
                             date=weekend_date)

    def test_price_defined(self):
        event = Event.objects.get(id=1)
        self.assertEqual(event.price, 6000)

    def test_upcoming(self):
        qs = Event.get_upcoming()
        self.assertIsInstance(qs, QuerySet)

    def test_event_month_schedule(self):
        qs = Event.get_event_month_schedule('TestEvent')

        today = datetime.today()
        date = qs[0].date

        self.assertIsInstance(qs, QuerySet)
        self.assertIs(today.month, date.month)

    def test_transaction(self):

        weekend_date = datetime.strptime('2019-12-29', '%Y-%m-%d')
        event = Event.objects.get(id=1)
        transaction = Transaction.objects.create(
            amount=1,
            date=weekend_date,
            event=event,
            transaction_id=111111
        )
        transaction.make_reserve()

        self.assertEqual(event.reserves, 99)


