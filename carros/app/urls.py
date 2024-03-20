"""
URL configuration for app project.

Aqui eu adiciono todas as rotas de URL do projeto
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_views
from cars.views import new_car_view
from accounts.views import register_view

# Local onde disponibilizamos as rotas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('cars/', cars_views, name='cars_list'),
    path('new_car/', new_car_view, name='new_car')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
