from django.urls import URLPattern, path
from . import views

urlpatterns = [path('show/', views.Product_list, name = 'show'),
               path('search/', views.Search, name = 'search'),
               path('', views.Form_in, name = 'login'),
               path('logout/', views.Form_out, name = 'logout'),
               path('add_to_cart/<int:id>', views.add_to_cart, name = 'add_to_cart'),
               path('cart/',views.Show_cart, name = 'cart'),
               path('del_cart/<int:id>',views.Remove_cart, name = 'del_cart'),
               
               ]


'''path('add/', views.Add_product, name= 'add'),path('new_cart/<int:id>',views.Product_quantity, name = 'new_cart')'''