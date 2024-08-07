from django.urls import path
from .views import RegisterAPI, UserAPI, ItemListCreateAPI, ItemDetailAPI, ExpenseListCreateAPI, ExpenseDetailAPI
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('user/', UserAPI.as_view(), name='user'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('items/', ItemListCreateAPI.as_view(), name='item_list_create'),
    path('items/<int:pk>/', ItemDetailAPI.as_view(), name='item_detail'),
    path('expenses/', ExpenseListCreateAPI.as_view(), name='expense_list_create'),
    path('expenses/<int:pk>/', ExpenseDetailAPI.as_view(), name='expense_detail'),
]
