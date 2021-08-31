from django.urls import path
from .views import FruitListView
from django.views.generic import RedirectView

urlpatterns = [
    path('fruit-list',FruitListView.as_view(), name='fruit-list'),
    path('', RedirectView.as_view(url='fruit-list')),
]