from .serializers import EventSerializer, TransactionSerializer
from rest_framework import generics, viewsets, status
from .models import Event, Transaction
from rest_framework.response import Response
from rest_framework.views import APIView


class UpcomingEvents(viewsets.ModelViewSet):
    """
    Получаем список мероприятий
    """
    queryset = Event.get_upcoming()
    serializer_class = EventSerializer


class RetrieveEvent(generics.RetrieveAPIView):
    """
    Получаем данные конкретного события по айдишнику
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class RetrieveEventSchedule(viewsets.ModelViewSet):
    """
    Получаем расписание конкретного события на месяц
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        event_title = self.request.data.get('event_title')
        qs = Event.get_event_month_schedule(event_title)
        return qs


class MakeTransaction(APIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        amount = request.data.get('amount')
        event_id = request.data.get('event')
        transaction_id = request.data.get('transaction_id')

        try:
            event = Event.objects.get(id=event_id)

            tr = Transaction.objects.create(
                amount=amount,
                event=event,
                transaction_id=transaction_id
            )
            try:
                tr.make_reserve()
                tr.save()
                return Response({''}, status=status.HTTP_200_OK)

            except ValueError:
                return Response({'Нехватает билетов'}, status=status.HTTP_400_BAD_REQUEST)

        except Event.DoesNotExist:
            return Response({'Нет такого события'}, status=status.HTTP_400_BAD_REQUEST)

