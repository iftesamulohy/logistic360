from . import views
from django.urls import path


urlpatterns = [
    path("",views.Index.as_view(),name="home"),
    path("about",views.About.as_view(),name="about"),
    path("services",views.Service.as_view(),name="services"),
    path("contact",views.Contact.as_view(),name="contact"),
    path("login",views.Login.as_view(),name="login"),
    path("dashboard",views.Dashboard.as_view(),name="dashboard"),
    path("my-delivery",views.DeliveryList.as_view(),name="my-delivery"),
    path("logout",views.logout_pages,name = 'logout')


    
    
]