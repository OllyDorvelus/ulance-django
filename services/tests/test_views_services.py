from django.test import TestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User

class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestViews, cls).setUpClass()
        cls.user = mixer.blend(User)
        cls.service = mixer.blend('services.ServiceModel')
        cls.review = mixer.blend('services.Service')
        cls.review = mixer.blend('services.ReviewModel')
        cls.review = mixer.blend