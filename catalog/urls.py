from .views import CatalogView, CatalogDetailView, HomePageView, ContactPageView, PayPageView, DeliveryPageView, \
    FeedBackPageView, PartsListView, PartSearchListView, CartPageView, DetailSearchView, cart_add, cart_clear, \
    item_clear, item_increment, item_decrement, payment
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('feedback/', FeedBackPageView.as_view(), name='feedback'),
    path('pay/', PayPageView.as_view(), name='pay_page'),
    path('delivery/', DeliveryPageView.as_view(), name='delivery'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('catalog/search/', PartSearchListView.as_view(), name='search'),
    path('catalog/detail/search/', DetailSearchView.as_view(), name='search_details'),
    path('catalog/<slug:slug>/', CatalogDetailView, name='details'),
    path('catalog/<slug:slug>/<slug:category>/', PartsListView, name='cart'),
    path('cart/',  CartPageView, name='basket'),
    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/payment/', payment, name='payment')
]
