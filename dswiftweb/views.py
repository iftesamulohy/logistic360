
from django.template import loader
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from urllib.request import urlopen
from django.contrib.auth.models import User, auth
import json
from django.core.mail import send_mail
from django.views.generic.base import TemplateView

from dswiftweb.models import DeliveryItems
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class Index(TemplateView):
    template_name = "dswiftweb/index.html"
class About(TemplateView):
    template_name = "dswiftweb/about.html"
class Service(TemplateView):
    template_name = "dswiftweb/service.html"
class Contact(TemplateView):
    template_name = "dswiftweb/contact.html"
class Login(TemplateView):
    template_name = "dswiftweb/pages-login.html"
    def post(self, request, *args, **kwargs):
        username = request.POST['phone']
        password = request.POST['pass']
        print(username)
        print(password)
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            return redirect('login')
class Dashboard(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name = "dswiftweb/dashboard.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pending']=DeliveryItems.objects.filter(status='Pending',assigned_deliveryman=self.request.user).count()
        context['on_the_way']=DeliveryItems.objects.filter(status='On The Way',assigned_deliveryman=self.request.user).count()
        context['confirmed']=DeliveryItems.objects.filter(status='Confirmed',assigned_deliveryman=self.request.user).count()
        context['returned']=DeliveryItems.objects.filter(status='Returned',assigned_deliveryman=self.request.user).count()
        context['due']=DeliveryItems.objects.filter(payment_status='Due',assigned_deliveryman=self.request.user).count()
        context['paid']=DeliveryItems.objects.filter(payment_status='Completed',assigned_deliveryman=self.request.user).count()
        return context
class DeliveryList(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name = "dswiftweb/delivery-list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_delivery'] = DeliveryItems.objects.filter(assigned_deliveryman=self.request.user)
        return context
######logout####
def logout_pages(request):
        auth.logout(request)
        return HttpResponseRedirect('/')

 