from django.urls import path
from . import views

urlpatterns = [
    path('recipes-panel/<int:pk>/', views.RecipeUserPanel.as_view(), name='recipe-panel'),
    path('recipes/slug/<str:slug>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipes/home/', views.RecipeListView.as_view(), name='recipe-list'),
    path('recipes/search/', views.RecipeListSearch.as_view(), name='recipe-search'),
]