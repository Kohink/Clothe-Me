from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Closet, Clothes

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


class ClosetUpdate(UpdateView):
    model = Closet
    fields = ['name', 'desc']


class ClosetDelete(DeleteView):
    model = Closet
    def get_success_url(self):
        return reverse('user_closet:index')


class ClothesCreate(CreateView):
    model = Clothes
    template_name = 'user_closet/clothes_form.html'
    fields = ['clothes_name', 'brand', 'color', 'type_cloth', 'size', 'image']

    def get_context_data(self, **kwargs):
        closet_number = self.kwargs['pk']
        context = super(ClothesCreate, self).get_context_data(**kwargs)
        context['closet'] = Closet.objects.get(id = closet_number)
        context['link_clothes_create'] = True
        context['header_text'] = "Add New Clothes"
        return context

    def form_valid(self, form):
        closet_number = self.kwargs['pk']
        form.instance.closet = Closet.objects.get(id = closet_number)
        return super(ClothesCreate, self).form_valid(form)