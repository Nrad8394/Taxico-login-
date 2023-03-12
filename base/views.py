from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render,redirect
from base.models import *
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def index(requests):
    return render(requests,'base/index.html') 
class customloginview(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('booking')
    
class registerpage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated = True
    success_url = reverse_lazy('bookings')
    
    def form_valid(self,form):
        user = form.save()
        
        if user is not None:
            login(self.request,user)
        return super(registerpage,self).form_valid(form)


class  bookinglist(LoginRequiredMixin,ListView):
    model = booking
    context_object_name = ' booking'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['bookings']= context['bookings'].filter(user=self.request.user)
        context['count'] = context['bookings'].filter(complete=False).count()
        
        search_input = self.request.GET.get('search-area')or''
        if search_input:
            context['bookings'] = context['bookings'].filter(title__icontains= search_input)
            
        context['search_input'] = search_input    
          
        return context
    
    
class  bookingdetail(LoginRequiredMixin,DetailView) :
    model =  booking 
    context_object_name = 'booking'
    template_name = 'base/ booking.html'
    
class  bookingcreate(LoginRequiredMixin,CreateView):
    model =  booking
    fields = ['title','description','complete']
    success_url = reverse_lazy(' booking')
    
    def form_valid(self, form): 
        form.instance.user = self.request.user
        return super( bookingcreate,self).form_valid(form)
    
class  bookingupdate(LoginRequiredMixin,UpdateView):
    model =  booking
    fields = ['title','description','complete']
    success_url = reverse_lazy(' booking')
class  bookingdelete(LoginRequiredMixin,DeleteView):
    model =  booking
    context_object_name = ' booking'
    success_url = reverse_lazy(' booking')
