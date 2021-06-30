from django.urls import path
from . import views
from .views import InstallationDeleteView

app_name='installation'

urlpatterns = [
    path('table_installation/',views.table_installation,name='table_installation'),
#    path('ajouterD/', views.Ajout_D, name='ajouted'),
    path('install/',views.InstallationCreate,name='add_install'),
    path('detail_installation/<int:installation_id>/', views.InstallationDetail, name='detail_installation'),
    # path('detail_installation/<slug:pk>/delete/', InstallationDeleteView.as_view(), name='delete_installation'),
    path('update_installation/<int:installation_id>/update', views.InstallationUpdate, name='update_installation'),
    path('detail_installation/<int:installation_id>/delete/', views.InstallationDeleteView, name='delete_installation'),
    path('update_service/<int:service_id>/update', views.ServiceUpdate, name='update_service'),

]