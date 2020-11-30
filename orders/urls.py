from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from orders.views import Order, OrderItem, Order_view, Orderitems, Orders



urlpatterns = [
    path('makeorder/', Order.as_view()),
    path('makeorders/<usuario>/', Orders.as_view()),
    path('updateorder/<invoice_no>/', Order_view, name="invoice"),
    path('makeorder/post/', Order.as_view()),
    path('orderitems/<orden>/', Orderitems.as_view()),
    path('orderitem/post/', OrderItem.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)