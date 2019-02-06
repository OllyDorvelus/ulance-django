from django.urls import path
from . import views

app_name = 'services_api'

urlpatterns = [
    path('', views.ServiceListAPIView.as_view(), name='service-list-api'),
    path('categories/', views.CategoryListAPIView.as_view(), name='category-list-api'),
    path('category/create/', views.CategoryCreateAPIView.as_view(), name='category-create-api'),
    path('category/<pk>/', views.CategoryDetailAPIView.as_view(), name='category-detail-api'),
    path('main-categories', views.MainCategoryListAPIView.as_view(), name='main-category-list-api'),
    path('sub-categories/<pk>/', views.SubCategoryListAPIView.as_view(), name='sub-category-list-api'),
    path('create/', views.ServiceCreateAPIView.as_view(), name='service-create-api'),
    path('<pk>/', views.ServiceDetailAPIView.as_view(), name='service-detail-api'),
    path('<user__username>/services/', views.UserServiceListAPIView.as_view(), name='user-service-list-api'),
    path('<pk>/reviews/', views.ServiceReviewListAPIView.as_view(), name='service-reviews-list-api'),
    path('<pk>/review/create/', views.ReviewCreateAPIView.as_view(), name='review-create-api'),
    path('review/<pk>/', views.ReviewDetailAPIView.as_view(), name='review-detail-api'),
]