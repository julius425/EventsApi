import unittest
import requests


class Client:

    upcoming_url = 'http://127.0.0.1:8000/api/v1/events/'
    event_schedule_url = 'http://localhost:8000/api/v1/event/schedule/'
    transaction_url = 'http://127.0.0.1:8000/api/v1/event/transact/'

    def test_upcoming(self):
        # список всех запланированных мероприятий
        r = requests.get(self.upcoming_url)
        return r.json()

    def test_event_schedule(self):
        # расписание на месяц по названию ивента
        json = {'event_title': 'asdasd'}
        r = requests.get(self.event_schedule_url, json=json)
        return r.json()

    def test_transaction(self):
        # проводим транзакцию по айдишнику ивента
        json = {
            'event': 8,
            'amount': 1,
            'transaction_id': 999999,
        }

        r = requests.post(self.transaction_url, json=json)

        return r.json()

    def failed_transaction_amount(self):
        # фэил-тест количества забронированных мест
        json = {
            'event': 8,
            'amount': 1000,
            'transaction_id': 777777,
        }

        r = requests.post(self.transaction_url, json=json)
        return r.json()

    def failed_transaction_not_exists(self):
        # фэил-тест несуществующего ивента
        json = {
            'event': 9999,
            'amount': 1000,
            'transaction_id': 888888,
        }

        r = requests.post(self.transaction_url, json=json)

        return r.json()


if __name__ == '__main__':
    client = Client()

    from pprint import pprint
    upc = client.test_upcoming()
    sch = client.test_event_schedule()


    pprint(upc)
    pprint(sch)