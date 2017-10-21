from django.conf.urls import url
from .views import HotelView
urlpatterns = [
    url(r'^$', HotelView.as_view(), name='form'),
]