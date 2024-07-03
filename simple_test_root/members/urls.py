from . import views
from django.urls import path
from .views import CustomLoginView, CustomLogoutView

# Define URL patterns for the members model
urlpatterns = [
    path('login_user', views.login_user, name="login",),
    path('logout_user', views.logout_user, name="logout",),
    path('register_user', views.register_user, name="register_user",),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]