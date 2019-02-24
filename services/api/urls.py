from django.urls import path
from . import views

app_name = 'services_api'

urlpatterns = [
    path('', views.ServiceListAPIView.as_view(), name='service-list-api'),
    path('categories/', views.CategoryListAPIView.as_view(), name='category-list-api'),
    path('categories/create/', views.CategoryCreateAPIView.as_view(), name='category-create-api'),
    path('categories/<pk>/', views.CategoryDetailAPIView.as_view(), name='category-detail-api'),
    path('main-categories/', views.MainCategoryListAPIView.as_view(), name='main-category-list-api'),
    path('sub-categories/<pk>/', views.SubCategoryListAPIView.as_view(), name='sub-category-list-api'),
    path('<service_pk>/categories/', views.ServiceCategoryListAPIView.as_view(), name='service-category-list-api'),
    path('<service_pk>/remove/<category_pk>/', views.RemoveCategoryAPIView.as_view(), name='remove-category-api-view'),
    path('<service_pk>/add/<category_pk>/', views.AddCategoryAPIView.as_view(), name='add-category-api-view'),
    path('create/', views.ServiceCreateAPIView.as_view(), name='service-create-api'),
    path('<pk>/', views.ServiceDetailAPIView.as_view(), name='service-detail-api'),
    path('<user__username>/services/', views.UserServiceListAPIView.as_view(), name='user-service-list-api'),
    path('reviews/<pk>/', views.ReviewDetailAPIView.as_view(), name='review-detail-api'),
    path('<pk>/reviews/', views.ServiceReviewListAPIView.as_view(), name='service-reviews-list-api'),
    path('<pk>/reviews/create/', views.ReviewCreateAPIView.as_view(), name='review-create-api'),

]