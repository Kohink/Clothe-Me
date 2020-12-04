from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .models import Closet, Clothes
from .forms import RegisterForm, LoginForm

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


def Logout(request):
    logout(request)
    return redirect('/')



class UserLogin(FormView):
    form_class = LoginForm
    template_name = 'user_closet/registration_form.html'

    def get_context_data(self, **kwargs):
        context = super(UserLogin, self).get_context_data(**kwargs)
        context['header_text'] = 'Log In'
        context['login'] = True
        return context

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/closet/')
            else:
                return render(request, self.template_name, {'form': self.form_class(None), 'error_message': 'Inactive User', 'header_text': 'Log In', 'login': True})
        else: 
            return render(request, self.template_name, {'form': self.form_class(None), 'error_message': 'Invalid Credentials', 'header_text': 'Log In', 'login': True})


class UserRegister(FormView):
    form_class = RegisterForm
    template_name = 'user_closet/registration_form.html'

    def get_context_data(self, **kwargs):
        context = super(UserRegister, self).get_context_data(**kwargs)
        context['header_text'] = 'Register New Account'
        context['register_user'] = True
        return context

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit = False)

            # cleaned (normalized data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/closet/login/')

        return render(request, self.template_name, {'form': form, 'header_text': 'Register New Account', 'register_user': True})