from django.urls import path, include
from rest_framework import routers

from .views import (
    UpcomingEvents,
    RetrieveEvent,
    RetrieveEventSchedule,
    MakeTransaction,
)


router = routers.DefaultRouter()

router.register('events', UpcomingEvents, basename='upcoming_events')
router.register('event/schedule', RetrieveEventSchedule, basename='retrieve_event_schedule')


urlpatterns = [
    path('', include(router.urls)),
    path('event/<int:pk>/', RetrieveEvent.as_view(), name='retrieve_event'),
    path('event/transact/', MakeTransaction.as_view(), name='make_transaction')
]
