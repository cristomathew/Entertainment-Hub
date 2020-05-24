from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('subcategories/<int:pk>',views.subcategories,name='subcategories'),
    path('seasons/<int:pk>',views.seasons,name='seasons'),
    path('seasons/list/<int:pk>/',views.listview,name='list'),
    path('seasons/detail/<int:pk>',views.detail,name='detail'),

    path('login/',views.user_login,name='login')

]
