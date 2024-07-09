from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import RegisterView

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name="users/login.html"),
         name='login'
         ),
    path('registro/',
         RegisterView.as_view(template_name="users/register.html"),
         name='registrer'
         ),
    path('logout/',
         LogoutView.as_view(),
         name='logout'
         )
] 