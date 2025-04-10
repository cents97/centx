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
    path('products/category/<slug:category_slug>/', views.category_products, name='category_products'),
    path('video/', views.video_list, name='video'),
    path('faq/', views.faq_page, name='faq'),
]
