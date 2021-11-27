from django.urls import path
from .views import HomePageView, Xamerz

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),

]