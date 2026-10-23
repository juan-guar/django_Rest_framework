from django.urls import path
from . import views, class_views, generic_views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),

  path(
      'class/items/',
      class_views.ItemListAPIView.as_view(),
      name='class-item-list'
  ),
  path(
      'class/items/<int:pk>/',
      class_views.ItemDetailAPIView.as_view(),
      name='class-item-detail'
  ),

    # Vistas genéricas
        path(
            'generic/items/',
            generic_views.ItemListCreateAPIView.as_view(),
            name='generic-item-list',
        ),
        path(
            'generic/items/<int:pk>/',
            generic_views.ItemRetrieveUpdateDestroyAPIView.as_view(),
            name='generic-item-detail',
        ),

]



