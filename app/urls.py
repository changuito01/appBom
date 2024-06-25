from django.urls import path
from .views import registro_usuario, inventario, historial, actualizar_herramienta, registrar_herramienta, CustomLoginView
from . import views

urlpatterns = [

    path('index/', views.index, name='index'),

    path('accounts/login/', CustomLoginView.as_view(), name='login'),

    path('', views.index, name='index'),

    path('registro/', registro_usuario, name='registro_usuario'),

    path('inventario/', inventario, name='inventario'),

    path('historial/', historial, name='historial'),

    path('inventario/<int:pk>/actualizar/', actualizar_herramienta, name='actualizar_herramienta'),

    path('registrar_herramienta/', registrar_herramienta, name='registrar_herramienta'),

    path('inventario/<int:pk>/eliminar/', views.eliminar_herramienta, name='eliminar_herramienta'),


]
