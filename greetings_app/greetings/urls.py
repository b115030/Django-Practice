from django.urls import path
from .views import greeting_list, home_view, home

urlpatterns= [
    path('', greeting_list),
    path('', home_view),
    path('', home),
]