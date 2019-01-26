from django.test import TestCase
from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from mixer.backend.django import mixer
import pytest
from django.test import TestCase
from accounts.views import login, register

@pytest.mark.django_db
class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestViews, cls).setUpClass()
        cls.factory = RequestFactory()
        cls.no_user = AnonymousUser()

    def test_login_view(self):
        request = self.factory.get("login/")
        request.user = self.no_user
        response = login(request)
        assert response.status_code == 200

    def test_login_redirect_authenticated(self):
        request = self.factory.get("login/")
        request.user = mixer.blend(User)
        response = login(request)
        assert response.status_code == 302

    def test_register(self):
        request = self.factory.get("register/")
        request.user = self.no_user
        response = register(request)
        assert response.status_code == 200

    def test_register_redirect_authenticated(self):
        request = self.factory.get("register/")
        request.user = mixer.blend(User)
        response = register(request)
        assert response.status_code == 302


