from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Shop Home"),
    path('about/',views.about,name="About Us"),
    path('contact/',views.contact,name="Contact Us"),
    path('tracker/',views.tracker,name="Tracking Status"),
    path('search/',views.search,name="Search"),
    path('products/<int:myid>',views.productview,name="Product View"),
    path('checkout/',views.checkout,name="Check Out"),
    path('handlerequest/',views.handlerequest,name="Handle Request")
]
