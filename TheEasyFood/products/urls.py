from django.urls import path
from django.urls.conf import include
from .import views

urlpatterns = [
    path('homePage',views.homePage,name='homePage'),
    path('productDetails/<int:pk>/',views.productDetails, name='productDetails'),
    path('search',views.search,name='search'),
    path('checkout',views.checkout,name='checkout'),
    path('myOrders',views.myOrders,name='myOrders'), 
    path('myProfile/<int:pk>/',views.myProfile, name='myProfile'),
    path('about',views.about,name='about'), 
]