from django.urls import path

from .import views


urlpatterns = [

    path("singup",views.singup,name="singup"),
    path("login",views.login_form,name='login'),
    path("logout",views.user_logout,name="logout"),
    path("profile/",views.user_profile,name="profile"),
    
    
]
