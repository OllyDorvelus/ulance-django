from django.test import TestCase
from django.urls import reverse, resolve
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class TestModels(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestModels, cls).setUpClass()
        cls.user = mixer.blend(User, username='username')
        cls.user2 = mixer.blend(User, username='username2')
        cls.skill = mixer.blend('profiles.SkillModel', name='skill_name')
        cls.level = mixer.blend('profiles.LevelModel', name='level', user=cls.user, skill=cls.skill, skill_level='BG')
        cls.profile = mixer.blend('profiles.ProfileModel', user=cls.user)
        cls.profile2 = mixer.blend('profiles.ProfileModel', user=cls.user2)
        cls.link = mixer.blend('profiles.LinkModel', link='https://github.com/')
        cls.major = mixer.blend('profiles.MajorModel', name='major_name')
        cls.school = mixer.blend('profiles.SchoolModel', name='school_name')
        cls.education = mixer.blend('profiles.EducationModel', school=cls.school, major=cls.major)
        cls.certification = mixer.blend('profiles.CertificationModel', name='certification_name')
        cls.service = mixer.blend('services.ServiceModel', user=cls.user2)
        cls.service2 = mixer.blend('services.ServiceModel', user=cls.user2)
        cls.entry = mixer.blend('orders.EntryModel', status='COM', is_ordered=True, service=cls.service)
        cls.entry2 = mixer.blend('orders.EntryModel', status='COM', is_ordered=True, service=cls.service)
        cls.entry3 = mixer.blend('orders.EntryModel', status='COM', is_ordered=True, service=cls.service2)

    def test_skill_to_string(self):
        assert str(self.skill) == 'skill_name'

    def test_level_to_string(self):
        assert str(self.level) == 'skill_name - BG - username'

    def test_profile_to_string(self):
        assert str(self.profile) == 'username'

    def test_profile_get_absolute_url(self):
        path = self.profile.get_absolute_url()
        assert resolve(path).view_name == 'profiles:profile-detail'
        assert resolve(path).kwargs == {'username': self.profile.user.username}

    def test_profile_no_services_completed(self):
        assert self.profile.get_services_completed() == 0

    def test_profile_services_completed(self):
        assert self.profile2.get_services_completed() == 3

    def test_link_to_string(self):
        assert str(self.link) == 'https://github.com/'

    def test_major_to_string(self):
        assert str(self.major) == 'major_name'

    def test_school_to_string(self):
        assert str(self.school) == 'school_name'

    def test_education_to_string(self):
        assert str(self.education) == 'school_name - major_name'

    def test_certification_to_string(self):
        assert str(self.certification) == 'certification_name'


