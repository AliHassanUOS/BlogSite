from django.urls import path
from .import views



urlpatterns = [


    path("",views.home_page,name="home"),
    path("addblog/",views.add_blog,name='add_blog'),
    path("detail/<int:id>",views.PostDetail,name="detail"),
    path("editblog/<int:id>",views.editblog,name="editblog"),
    path("delete/<int:id>",views.deletblog,name="delete"),
    path("dashboard",views.dashboard,name="dashboard"),

]
