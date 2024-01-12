from django.urls import path

from for_main19.2.views import home, contacts

urlpatterns = [
    path('', home),
    path('contacts/', contacts)
]
