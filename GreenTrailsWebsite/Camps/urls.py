

from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('camp/',views.camps,name="camps"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('camp/<str:title>',views.camp_info,name="campInfo"),
    path('register/',views.registrationForm,name="register"),
    path('register/confirmation/',views.campConformation,name="conformation")
   
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)