from django.contrib import admin
from django.urls import path
from .views import test,login,signup,addtodo,signout,deletetodo,modtodo

urlpatterns = [
    path('', test,name='tester'),
    path('login/', login,name='login'),
    path('signup/', signup,name='signup'),
    path('add-todo/',addtodo,name='addtodo'),
    path('logout/',signout,name='logout'),
    path('delete-todo/<int:id>',deletetodo,name='delete'),
    path('change-status/<int:id>/<str:status>',modtodo,name='modtodo'),

]
