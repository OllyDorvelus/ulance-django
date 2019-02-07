from django.test import TestCase
from django.urls import reverse, resolve
from mixer.backend.django import mixer
from django.contrib.auth.models import User


class TestUrls(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestUrls, cls).setUpClass()
        cls.url = 'services'
        cls.api_url = 'services_api'
        cls.user = mixer.blend(User)
        cls.service = mixer.blend('services.ServiceModel')
        cls.category = mixer.blend('services.CategoryModel')
        cls.review = mixer.blend('services.ReviewModel')

    def test_service_detail_view(self):
        path = reverse(f'{self.url}:service-detail', kwargs={'pk': self.service.pk})
        assert resolve(path).view_name == f'{self.url}:service-detail'
        assert resolve(path).kwargs == {'pk': str(self.service.pk)}

    def test_api_service_list_view(self):
        path = reverse(f'{self.api_url}:service-list-api')
        assert resolve(path).view_name == f'{self.api_url}:service-list-api'

    def test_api_service_create_view(self):
        path = reverse(f'{self.api_url}:service-create-api')
        assert resolve(path).view_name == f'{self.api_url}:service-create-api'

    def test_api_service_detail_view(self):
        path = reverse(f'{self.api_url}:service-detail-api', kwargs={'pk': self.service.pk})
        assert resolve(path).view_name == f'{self.api_url}:service-detail-api'
        assert resolve(path).kwargs == {'pk': str(self.service.pk)}

    def test_api_category_list_view(self):
        path = reverse(f'{self.api_url}:category-list-api')
        assert resolve(path).view_name == f'{self.api_url}:category-list-api'

    def test_main_api_category_list_url(self):
        path = reverse(f'{self.api_url}:main-category-list-api')
        assert resolve(path).view_name == f'{self.api_url}:main-category-list-api'

    def test_sub_api_category_detail_list_url(self):
        path = reverse(f'{self.api_url}:sub-category-list-api', kwargs={'pk': self.category.pk})
        assert resolve(path).view_name == f'{self.api_url}:sub-category-list-api'
        assert resolve(path).kwargs == {'pk': str(self.category.pk)}

    def test_api_category_create_view(self):
        path = reverse(f'{self.api_url}:category-create-api')
        assert resolve(path).view_name == f'{self.api_url}:category-create-api'

    def test_api_category_detail_view(self):
        path = reverse(f'{self.api_url}:category-detail-api', kwargs={'pk': self.category.pk})
        assert resolve(path).view_name == f'{self.api_url}:category-detail-api'
        assert resolve(path).kwargs == {'pk': str(self.category.pk)}

    def test_api_service_reviews_list_view(self):
        path = reverse(f'{self.api_url}:service-reviews-list-api', kwargs={'pk': self.service.pk})
        assert resolve(path).view_name == f'{self.api_url}:service-reviews-list-api'
        assert resolve(path).kwargs == {'pk': str(self.service.pk)}

    def test_api_review_create_view(self):
        path = reverse(f'{self.api_url}:review-create-api', kwargs={'pk': self.service.pk})
        assert resolve(path).view_name == f'{self.api_url}:review-create-api'
        assert resolve(path).kwargs == {'pk': str(self.service.pk)}

    def test_api_review_detail_view(self):
        path = reverse(f'{self.api_url}:review-detail-api', kwargs={'pk': self.review.pk})
        assert resolve(path).view_name == f'{self.api_url}:review-detail-api'
        assert resolve(path).kwargs == {'pk': str(self.review.pk)}





















