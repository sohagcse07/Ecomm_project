from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login/', views.login_page , name="login"),
    path('register/', views.register_page , name="register"),
    path('activate/<str:email_token>/', views.activite_email , name="activite_email"),
    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)