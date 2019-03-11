from django.urls import path
from . import views

app_name = 'services_api'

urlpatterns = [
    path('', views.ServiceListAPIView.as_view(), name='service-list-api'),
    path('create/', views.ServiceCreateAPIView.as_view(), name='service-create-api'),
    path('categories/', views.CategoryListAPIView.as_view(), name='category-list-api'),
    path('categories/create/', views.CategoryCreateAPIView.as_view(), name='category-create-api'),
    path('categories/<pk>/', views.CategoryDetailAPIView.as_view(), name='category-detail-api'),
    path('categories/<category_name>/services/', views.CategoryServiceListAPIView.as_view(), name='category-service-list-api'),
    path('main-categories/', views.MainCategoryListAPIView.as_view(), name='main-category-list-api'),
    path('sub-categories/<pk>/', views.SubCategoryListAPIView.as_view(), name='sub-category-list-api'),
    path('jobs/', views.JobListAPIView.as_view(), name='job-list-api'),
    path('jobs/create/', views.JobCreateAPIView.as_view(), name='job-create-api'),
    path('jobs/<pk>', views.JobDetailAPIView.as_view(), name='job-detail-api'),
    path('<service_pk>/categories/', views.ServiceCategoryListAPIView.as_view(), name='service-category-list-api'),
    path('<service_pk>/remove/<category_pk>/', views.RemoveCategoryAPIView.as_view(), name='remove-category-api-view'),
    path('<service_pk>/add/<category_pk>/', views.AddCategoryAPIView.as_view(), name='add-category-api-view'),

    path('<pk>/', views.ServiceDetailAPIView.as_view(), name='service-detail-api'),
    path('<user__username>/services/', views.UserServiceListAPIView.as_view(), name='user-service-list-api'),
    #  path('job/<job_pk>/categories/', views.JobCategoryListAPIView.as_view(), name='job-category-list-api'),
    path('jobs/categories/<job_pk>/remove/<category_pk>/', views.RemoveJobCategoryAPIView.as_view(),
         name='remove-job-category-api-view'),
    path('jobs/categories/<job_pk>/add/<category_pk>/', views.AddJobCategoryAPIView.as_view(),
         name='add-job-category-api-view'),
    path('jobs/skills/<job_pk>/remove/<skill_pk>/', views.RemoveJobSkillAPIView.as_view(),
         name='remove-job-category-api-view'),
    path('jobs/skills/<job_pk>/add/<skill_pk>/', views.AddJobSkillAPIView.as_view(),
         name='add-job-category-api-view'),
    path('reviews/<pk>/', views.ReviewDetailAPIView.as_view(), name='review-detail-api'),
    path('<pk>/reviews/', views.ServiceReviewListAPIView.as_view(), name='service-reviews-list-api'),
    path('<pk>/reviews/create/', views.ReviewCreateAPIView.as_view(), name='review-create-api'),

]