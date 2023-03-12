from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login/', customloginview.as_view(),name='login'),
    path('register/', registerpage.as_view(),name='register'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('',index,name='index'),
    
    path('main', bookinglist.as_view(),name='booking'),
    path(' booking/<int:pk>/',  bookingdetail.as_view(),name='bookings'),
    path(' booking-create/', bookingcreate.as_view(),name='booking-create'),
    path(' booking-update/<int:pk>/',  bookingupdate.as_view(),name='booking-update'),
    path(' booking-delete/<int:pk>/',  bookingdelete.as_view(),name='booking-delete'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



