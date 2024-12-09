from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('filmlog/<int:pk>', views.movie_log, name='filmlog'),
    path('delete_filmlog/<int:pk>', views.delete_filmlog, name='delete_filmlog'),
    path('add_filmlog/', views.add_filmlog, name='add_filmlog'),
    path('update_filmlog/<int:pk>', views.update_filmlog, name='update_filmlog'),
    path('search_venues', views.search_venues, name='search-venues'),
]