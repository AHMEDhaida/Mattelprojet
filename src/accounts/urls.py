from django.urls import include, path
from . import views
app_name = 'app'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', views.loginPage, name='login'),
    path('login/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/ajout', views.Ajouterprofile, name='profile_ajout'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('change_password/', views.change_password, name='change_password'),
    path('User/<int:pk>/Role', views.Rolesuperuser, name='roleuser'),
    
]