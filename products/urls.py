from django.urls import path
from . import views


urlpatterns = [
    path('create',views.create,name='create'),
    path('products/<int:product_id>',views.detail,name='detail'),
    path('products/<int:product_id>/upvote',views.upvote,name='upvote'),
]