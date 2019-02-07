from django.test import TestCase
from django.urls import reverse, resolve
from mixer.backend.django import mixer
from django.contrib.auth.models import User
import pytest


class TestModels(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestModels, cls).setUpClass()
        cls.service = mixer.blend('services.ServiceModel')
        cls.category = mixer.blend('services.CategoryModel', name='category_name', is_parent=True)
        cls.child_category = mixer.blend('services.CategoryModel', name='child_category', is_parent=False, parent=cls.category)
        cls.child_category2 = mixer.blend('services.CategoryModel', name='child_category2', is_parent=False, parent=cls.category)

    def test_category_get_name(self):
        assert self.category.get_name == 'category_name'

    def test_category_get_all_sub_categories_for_child_category(self):
        assert self.child_category.get_all_sub_categories() == []

    def test_category_get_all_sub_categories_for_parent_category(self):
        all_children = self.category.get_all_sub_categories()
        assert all_children.count() == 2

    def test_service_absolute_url(self):
        path = self.service.get_absolute_url()
        assert resolve(path).view_name == 'services:service-detail'
        assert resolve(path).kwargs == {'pk': str(self.service.pk)}




