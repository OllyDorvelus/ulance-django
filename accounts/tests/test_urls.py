from django.test import TestCase
from django.urls import reverse, resolve


class TestUrls(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestUrls, cls).setUpClass()
        cls.url = 'accounts'
        cls.api_url = 'accounts_api'

    def test_login_url(self):
        path = reverse(f'{self.url}:login')
        assert resolve(path).view_name == f'{self.url}:login'

    def test_register_url(self):
        path = reverse(f'{self.url}:register')
        assert resolve(path).view_name == f'{self.url}:register'

    def test_api_url(self):
        path = reverse(f'{self.api_url}:accounts-api')
        assert resolve(path).view_name == f'{self.api_url}:accounts-api'

    def test_register_api_url(self):
        path = reverse(f'{self.api_url}:accounts-register-api')
        assert resolve(path).view_name == f'{self.api_url}:accounts-register-api'

    def test_login_api_url(self):
        path = reverse(f'{self.api_url}:accounts-login-api')
        assert resolve(path).view_name == f'{self.api_url}:accounts-login-api'
