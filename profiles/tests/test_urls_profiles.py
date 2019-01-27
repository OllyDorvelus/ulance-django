from django.test import TestCase
from django.urls import reverse, resolve
from mixer.backend.django import mixer
from django.contrib.auth.models import User


class TestUrls(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestUrls, cls).setUpClass()
        cls.url = 'profiles'
        cls.api_url = 'profiles_api'
        cls.user = mixer.blend(User)
        cls.user.username = 'testname'
        cls.profile = mixer.blend('profiles.ProfileModel')
        cls.profile.user = cls.user
        cls.skill = mixer.blend('profiles.SkillModel')
        cls.link = mixer.blend('profiles.LinkModel')
        cls.level = mixer.blend('profiles.LevelModel')
        cls.certification = mixer.blend('profiles.CertificationModel')
        cls.education = mixer.blend('profiles.EducationModel')
        cls.major = mixer.blend('profiles.MajorModel')
        cls.school = mixer.blend('profiles.SchoolModel')

    def test_profile_detail_view(self):
        path = reverse(f'{self.url}:profile-detail', kwargs={'username': self.user.username})
        assert resolve(path).view_name == f'{self.url}:profile-detail'
        assert resolve(path).kwargs == {'username': self.user.username}

    def test_api_profile_list_view(self):
        path = reverse(f'{self.api_url}:profile-list-api')
        assert resolve(path).view_name == f'{self.api_url}:profile-list-api'

    def test_api_profile_detail_view(self):
        path = reverse(f'{self.api_url}:profile-detail-api', kwargs={'user__username': self.profile.user.username})
        assert resolve(path).view_name == f'{self.api_url}:profile-detail-api'
        assert resolve(path).kwargs == {'user__username': self.profile.user.username}

    def test_api_skill_list_view(self):
        path = reverse(f'{self.api_url}:skill-list-api')
        assert resolve(path).view_name == f'{self.api_url}:skill-list-api'

    def test_api_skill_create_view(self):
        path = reverse(f'{self.api_url}:skill-create-api')
        assert resolve(path).view_name == f'{self.api_url}:skill-create-api'

    def test_api_skill_detail_view(self):
        path = reverse(f'{self.api_url}:skill-detail-api', kwargs={'pk': self.skill.pk})
        assert resolve(path).view_name == f'{self.api_url}:skill-detail-api'
        assert resolve(path).kwargs == {'pk': str(self.skill.pk)}

    def test_api_link_list_view(self):
        path = reverse(f'{self.api_url}:link-create-api')
        assert resolve(path).view_name == f'{self.api_url}:link-create-api'

    def test_api_link_detail_view(self):
        path = reverse(f'{self.api_url}:link-detail-api', kwargs={'pk': self.link.pk})
        assert resolve(path).view_name == f'{self.api_url}:link-detail-api'
        assert resolve(path).kwargs == {'pk': str(self.link.pk)}

    def test_api_link_create_view(self):
        path = reverse(f'{self.api_url}:link-create-api')
        assert resolve(path).view_name == f'{self.api_url}:link-create-api'

    def test_api_portfolio_create_view(self):
        path = reverse(f'{self.api_url}:portfolio-create-api')
        assert resolve(path).view_name == f'{self.api_url}:portfolio-create-api'

    def test_api_user_portfolio_detail_view(self):
        path = reverse(f'{self.api_url}:portfolio-detail-api', kwargs={'user__username': self.profile.user.username})
        assert resolve(path).view_name == f'{self.api_url}:portfolio-detail-api'
        assert resolve(path).kwargs == {'user__username': self.profile.user.username}

    def test_api_level_create_view(self):
        path = reverse(f'{self.api_url}:level-create-api')
        assert resolve(path).view_name == f'{self.api_url}:level-create-api'

    def test_api_level_detail_view(self):
        path = reverse(f'{self.api_url}:level-detail-api', kwargs={'pk': self.level.pk})
        assert resolve(path).view_name == f'{self.api_url}:level-detail-api'
        assert resolve(path).kwargs == {'pk': str(self.level.pk)}

    def test_api_user_level_list_view(self):
        path = reverse(f'{self.api_url}:user-level-list-api', kwargs={'user__username': self.profile.user.username})
        assert resolve(path).view_name == f'{self.api_url}:user-level-list-api'
        assert resolve(path).kwargs == {'user__username': self.profile.user.username}

    def test_api_certification_create_view(self):
        path = reverse(f'{self.api_url}:certification-create-api')
        assert resolve(path).view_name == f'{self.api_url}:certification-create-api'

    def test_api_certification_detail_view(self):
        path = reverse(f'{self.api_url}:certification-detail-api', kwargs={'pk': self.certification.pk})
        assert resolve(path).view_name == f'{self.api_url}:certification-detail-api'
        assert resolve(path).kwargs == {'pk': str(self.certification.pk)}

    def test_api_user_certification_list_view(self):
        path = reverse(f'{self.api_url}:user-certification-list-api', kwargs={'user__username': self.profile.user.username})
        assert resolve(path).view_name == f'{self.api_url}:user-certification-list-api'
        assert resolve(path).kwargs == {'user__username': self.profile.user.username}

    def test_api_education_create_view(self):
        path = reverse(f'{self.api_url}:education-create-api')
        assert resolve(path).view_name == f'{self.api_url}:education-create-api'

    def test_api_education_detail_view(self):
        path = reverse(f'{self.api_url}:education-detail-api', kwargs={'pk': self.education.pk})
        assert resolve(path).view_name == f'{self.api_url}:education-detail-api'
        assert resolve(path).kwargs == {'pk': str(self.education.pk)}

    def test_api_user_education_list_view(self):
        path = reverse(f'{self.api_url}:user-education-list-api', kwargs={'user__username': self.profile.user.username})
        assert resolve(path).view_name == f'{self.api_url}:user-education-list-api'
        assert resolve(path).kwargs == {'user__username': self.profile.user.username}

    def test_api_major_create_view(self):
        path = reverse(f'{self.api_url}:major-create-api')
        assert resolve(path).view_name == f'{self.api_url}:major-create-api'

    def test_api_major_create_view(self):
        path = reverse(f'{self.api_url}:major-list-api')
        assert resolve(path).view_name == f'{self.api_url}:major-list-api'

    # def test_api_major_detail_view(self):
    #     path = reverse(f'{self.api_url}:major-detail-api', kwargs={'pk': self.major.pk})
    #     assert resolve(path).view_name == f'{self.api_url}:major-detail-api'
    #     assert resolve(path).kwargs == {'pk': str(self.major.pk)}

    def test_api_school_create_view(self):
        path = reverse(f'{self.api_url}:school-create-api')
        assert resolve(path).view_name == f'{self.api_url}:school-create-api'

    def test_api_school_list_view(self):
        path = reverse(f'{self.api_url}:school-list-api')
        assert resolve(path).view_name == f'{self.api_url}:school-list-api'

    # def test_api_school_detail_view(self):
    #     path = reverse(f'{self.api_url}:school-detail-api', kwargs={'pk': self.school.pk})
    #     assert resolve(path).view_name == f'{self.api_url}:school-detail-api'
    #     assert resolve(path).kwargs == {'pk': str(self.school.pk)}

















