from django.test import TestCase
from django.urls import reverse, resolve
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import pytest


class TestModels(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestModels, cls).setUpClass()
        cls.user = mixer.blend(User, username='username')
        cls.service = mixer.blend('services.ServiceModel', name='service')
        cls.review_service = mixer.blend('services.ServiceModel')
        cls.category = mixer.blend('services.CategoryModel', name='category_name', is_parent=True)
        cls.child_category = mixer.blend('services.CategoryModel', name='child_category', is_parent=False,
                                         parent=cls.category)
        cls.child_category2 = mixer.blend('services.CategoryModel', name='child_category2', is_parent=False,
                                          parent=cls.category)
        cls.review1 = mixer.blend('services.ReviewModel', rate=6, service=cls.review_service, user=cls.user)
        cls.review2 = mixer.blend('services.ReviewModel', rate=3, service=cls.review_service, description='aaaa',
                                  user=cls.user)
        cls.entry = mixer.blend('orders.EntryModel', is_ordered=True, service=cls.review_service)
        cls.entry2 = mixer.blend('orders.EntryModel', is_ordered=True, service=cls.review_service)

    def test_category_get_name(self):
        assert self.category.get_name == 'category_name'

    def test_category_get_all_sub_categories_for_child_category(self):
        assert self.child_category.get_all_sub_categories() == []

    def test_category_get_all_sub_categories_for_parent_category(self):
        all_children = self.category.get_all_sub_categories()
        assert all_children.count() == 2

    def test_parent_category_to_string(self):
        assert str(self.category) == 'category_name'

    def test_child_category_to_string(self):
        assert str(self.child_category) == 'category_name - child_category'

    def test_service_absolute_url(self):
        path = self.service.get_absolute_url()
        assert resolve(path).view_name == 'services:service-detail'
        assert resolve(path).kwargs == {'pk': str(self.service.pk)}

    def test_service_with_no_reviews_get_avg_rating(self):
        assert self.service.get_avg_rating() == 0

    def test_service_with_reviews_avg_rating(self):
        assert self.review_service.get_avg_rating() == 4.5

    def test_service_with_no_purchases(self):
        assert self.service.get_purchases() == 0

    def test_service_with_purchases(self):
        assert self.review_service.get_purchases() == 2

    def test_service_to_string(self):
        assert str(self.service) == 'service'

    def test_review_to_string(self):
        assert str(self.review1) == 'username - 6'

    def test_only_one_review(self):
        self.assertRaises(ValidationError, self.review2.clean)








