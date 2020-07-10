from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="market-home"),
    path('seller/<str:seller>', UserPostListView.as_view(), name="seller-items"),
    path('item/<int:pk>/', PostDetailView.as_view(), name="item-detail"),
    path('item/new/', PostCreateView.as_view(), name='item-create'),
    path('item/<int:pk>/update/', PostUpdateView.as_view(), name='item-update'),
    path('item/<int:pk>/delete/', PostDeleteView.as_view(), name='item-delete'),
    path('about/', views.about, name="market-about")
]