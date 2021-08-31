from django.views.generic import ListView
from .models import Fruit
from django.contrib.auth.mixins import LoginRequiredMixin

class FruitListView(LoginRequiredMixin, ListView):
    model = Fruit    
    template_name = 'catalogue/fruit-list.html'
    context_object_name = 'fruits'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['title'] = 'Fruit List'
        return context