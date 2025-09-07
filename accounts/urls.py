from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('reset/', views.reset_view, name='reset'),
    path('logout/', views.logout_view, name='logout'),
    path('set-password/', views.set_password_view, name='set_password'),
    path('admin/users/', views.admin_users_view, name='admin_users'),
    path('admin/users/<str:user_id>/update/', views.admin_update_user_view, name='admin_update_user'),
]
