from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('project/', views.project, name='project'),
    path('product/<int:product_id>/request/', views.request_product, name='request_product'),
    path('products/', views.all_products, name='all_products'),  # View all products
    path("save-message/", views.save_contact_message, name="save_message"),
]
