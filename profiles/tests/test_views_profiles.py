# from django.test import RequestFactory
# from django.contrib.auth.models import User, AnonymousUser
# from mixer.backend.django import mixer
# import pytest
# from django.test import TestCase
# from profiles.api.views import ProfileListAPIView, ProfileSerializer
#
# #
# #
# @pytest.mark.django_db
# class TestViews(TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         super(TestViews, cls).setUpClass()
#         cls.no_user = AnonymousUser()
#         cls.factory = RequestFactory()
#         cls.api_url = 'api/profiles/'
#         cls.skill = mixer.blend('profiles.SkillModel', name='skill_name')
#         cls.school = mixer.blend('profiles.SchoolModel', name='school_name')
#         cls.major = mixer.blend('profiles.MajorModel', name='major_name')
#
#     def test_profile_list_api_view(self):
#         request = self.factory.get(f'{self.api_url}')
#         view_func = ProfileListAPIView.as_view()
#         response = view_func(request)
#         assert response.status_code == 200
#
#
