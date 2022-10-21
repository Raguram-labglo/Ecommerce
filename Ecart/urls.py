from django.urls import URLPattern, path
from . import views

urlpatterns = [path('show/', views.Product_list, name = 'show'),
               path('search/', views.Search, name = 'search'),
               path('', views.Form_in, name = 'login'),
               path('logout/', views.Form_out, name = 'logout')]


'''path('add/', views.Add_product, name= 'add'),'''