from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Closet

class IndexView(generic.ListView):
    template_name = 'user_closet/index.html'
    context_object_name = 'all_closets'

    def get_queryset(self):
        return Closet.objects.all()


class DetailView(generic.DetailView):
    model = Closet
    template_name = 'user_closet/detail.html'


class ClosetCreate(CreateView):
    model = Closet
    fields = ['name', 'desc']