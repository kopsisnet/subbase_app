from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('reset/', views.reset_view, name='reset'),
    path('update-password/', views.update_password_view, name='update_password'),
]
