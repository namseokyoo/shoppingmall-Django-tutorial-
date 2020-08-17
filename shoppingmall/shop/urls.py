from django.urls import path
from . import views

urlpatterns = [
    # ex: shop/     (main item list page)
    path('', views.index, name='index'),
    # ex: shop/2    (item-order page)
    path('<int:item_id>/',views.itemdetail, name = 'itemdetail'),
    # ex: shop/orderlist    (order list page)
    path('orderlist/',views.orderlist,name ='orderlist')
]
