from django.test import RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from mixer.backend.django import mixer
import pytest
from django.test import TestCase
from accounts.views import login, register
from accounts.api.views import UserModelListAPIView, UserCreateAPIView


@pytest.mark.django_db
class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestViews, cls).setUpClass()
        cls.factory = RequestFactory()
        cls.no_user = AnonymousUser()
        cls.user = {
                "username": "sample_user",
                "email": "sample_user@sample.com",
                "email2": "sample_user@sample.com",
                "password": "my_password",
                "password2": "my_password"
        }

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

    def test_accounts_api(self):
        request = self.factory.get("api/accounts/")
        view_func = UserModelListAPIView.as_view()
        response = view_func(request)
        assert response.status_code == 200

    def test_user_create_api(self):

        request = self.factory.post("api/register/", self.user)
        view_func = UserCreateAPIView.as_view()
        response = view_func(request)
        assert response.status_code == 201

    def test_register_user_password_no_match(self):
        temp_user = dict(self.user)
        temp_user['password2'] = 'not_same'
        request = self.factory.post("api/register", temp_user)
        view_func = UserCreateAPIView.as_view()
        response = view_func(request)
        assert response.status_code == 400

    def test_register_user_email_no_match(self):
        temp_user = dict(self.user)
        temp_user['email'] = 'not_same@not_same.com'
        request = self.factory.post("api/register", temp_user)
        view_func = UserCreateAPIView.as_view()
        response = view_func(request)
        assert response.status_code == 400





