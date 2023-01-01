from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homePage),
    path('contact/',views.contactus,name='contactus'),
    path('thankyou/',views.thanks,name='thanks'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contactus/',views.contactus,name='contact'),
    path('navbar/',views.navbar,name='contact')
    


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)