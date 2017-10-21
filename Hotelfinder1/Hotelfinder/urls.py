from django.conf.urls import include,url
from django.contrib import admin
from hotelApp import urls as hotelUrls


urlpatterns = [
    url(r'^form/', include(hotelUrls)),
    url(r'^admin/', admin.site.urls),
]
