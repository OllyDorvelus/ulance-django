from django.urls import path
from . import views

app_name = 'profiles_api'

urlpatterns = [
    path('', views.ProfileListAPIView.as_view(), name='profile-list-api'),
    path('<user__username>/update/', views.ProfileUpdateAPIView.as_view(), name='profile-create-api'),
    path('user/<user__username>/', views.ProfileDetailAPIView.as_view(), name='profile-detail-api'),
    path('user/<user__username>/picture/', views.ProfilePictureDetailAPIView.as_view(), name='profile-pciture-detail-api'),
    path('skills/', views.SkillListAPIView.as_view(), name='skill-list-api'),
    path('skills/create/', views.SkillCreateAPIView.as_view(), name='skill-create-api'),
    path('skills/<pk>/', views.SkillDetailAPIView.as_view(), name='skill-detail-api'),
  #  path('links/', views.LinkListAPIView.as_view(), name='link-list-api'),
    path('links/create/', views.LinkCreateAPIView.as_view(), name='link-create-api'),
    path('links/<pk>/', views.LinkDetailAPIView.as_view(), name='link-detail-api'),
    path('<user__username>/links/', views.UserLinkListAPIView.as_view(), name='user-link-list-api'),
   # path('<user__username/')
    path('portfolio/create/', views.PortfolioCreateAPIView.as_view(), name='portfolio-create-api'),
    path('<user__username>/portfolio', views.PortfolioDetailAPIView.as_view(), name='portfolio-detail-api'),
    path('main-skills/', views.MainSkillListAPIView.as_view(), name='main-skill-list-api'),
    path('sub-skills/<pk>/', views.SubSkillListAPIView.as_view(), name='sub-skill-list-api'),
    path('skills/<profile_pk>/add/<skill_pk>/', views.AddSkillAPIView.as_view(), name='add-skill-api'),
    path('skills/<profile_pk>/remove/<skill_pk>/', views.RemoveSkillAPIView.as_view(), name='remove-skill-api'),
    path('<user__username>/skills/', views.UserSkillListAPIView.as_view(), name='user-skill-list-api'),
    path('certifications/create/', views.CertificationCreateAPIView.as_view(), name='certification-create-api'),
    path('certifications/<pk>/', views.CertificationDetailAPIView.as_view(), name='certification-detail-api'),
    path('<user__username>/certifications/', views.UserCertificationListAPIView.as_view(), name='user-certification-list-api'),
    path('educations/create/', views.EducationCreateAPIView.as_view(), name='education-create-api'),
    path('<user__username>/educations/', views.UserEducationListAPIView.as_view(), name='user-education-list-api'),
    path('educations/<pk>/', views.EducationDetailAPIView.as_view(), name ='education-detail-api'),
    path('majors/create/', views.MajorCreateAPIView.as_view(), name='major-create-api'),
    path('majors/', views.MajorListAPIView.as_view(), name='major-list-api'),
    path('schools/create/', views.SchoolCreateAPIView.as_view(), name='school-create-api'),
    path('schools/', views.SchoolListAPIView.as_view(), name='school-list-api')
]
