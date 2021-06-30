from django.urls import include, path
from . import views
app_name = 'equipement'

urlpatterns = [
    path('', views.home, name='home'),
    path('listequipement', views.listEquipement, name='listE'),
    path('listeuser', views.listuser, name='listU'),
    path('ajouter/', views.Ajout_E, name='ajoute'),
    # equipement
    path('add_equipement/', views.EquipementCreate, name='add_equipement'),
    path('detail_equipement/<int:equipement_id>/', views.EquipementDetail, name='detail_equipement'),
    path('detail_user/<int:user_id>/', views.UserDetail, name='detail_user'),
    path('update_equipement/<int:equipement_id>/update', views.EquipementUpdate, name='update_equipement'),
    path('detail_equipement/<int:equipement_id>/delete/', views.EquipementDeleteView, name='delete_equipement'),
    path('detail_user/<int:user_id>/delete/', views.UserDeleteView, name='delete_user'),

    # categorie
    path('category_table/', views.category_table, name='category_table'),
    path('add_categorie/', views.CategorietCreate, name='add_categorie'),
    path('update_categorie/<int:categorie_id>/update', views.CategoryUpdate, name='update_categorie'),

    # direction
    path('add_direction/', views.DirectionCreate, name='add_direction'),
    path('update_direction/<int:direction_id>/update', views.DirectionUpdate, name='update_direction'),

    path('pie/', views.pie_chart, name='pie'),

]