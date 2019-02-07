from django.test import TestCase
from django.urls import reverse, resolve
from mixer.backend.django import mixer
from django.contrib.auth.models import User


class TestUrls(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestUrls, cls).setUpClass()
        cls.url = 'orders'
        cls.api_url = 'orders_api'
        cls.entry = mixer.blend('orders.EntryModel')
        cls.service_order = mixer.blend('orders.ServiceOrderModel')
        cls.complaint = mixer.blend('orders.ComplaintModel')
        cls.service = mixer.blend('services.ServiceModel')

    def test_api_order_list_view(self):
        path = reverse(f'{self.api_url}:order-list-api')
        assert resolve(path).view_name == f'{self.api_url}:order-list-api'

    def test_api_order_create_view(self):
        path = reverse(f'{self.api_url}:order-create-api')
        assert resolve(path).view_name == f'{self.api_url}:order-create-api'

    def test_api_request_list_view(self):
        path = reverse(f'{self.api_url}:request-list-api')
        assert resolve(path).view_name == f'{self.api_url}:request-list-api'

    def test_api_cart_detail_view(self):
        path = reverse(f'{self.api_url}:cart-detail-api')
        assert resolve(path).view_name == f'{self.api_url}:cart-detail-api'

    def test_api_complaint_create_view(self):
        path = reverse(f'{self.api_url}:complaint-create-api', kwargs={'entry_id': self.entry.pk})
        assert resolve(path).view_name == f'{self.api_url}:complaint-create-api'
        assert resolve(path).kwargs == {'entry_id': str(self.entry.pk)}

    def test_api_complaint_detail_view(self):
        path = reverse(f'{self.api_url}:complaint-detail-api', kwargs={'pk': self.complaint.pk})
        assert resolve(path).view_name == f'{self.api_url}:complaint-detail-api'
        assert resolve(path).kwargs == {'pk': str(self.complaint.pk)}

    def test_api_entry_detail_view(self):
        path = reverse(f'{self.api_url}:entry-detail-api', kwargs={'pk': self.entry.pk})
        assert resolve(path).view_name == f'{self.api_url}:entry-detail-api'
        assert resolve(path).kwargs == {'pk': str(self.entry.pk)}

    def test_api_entry_service_detail_view(self):
        path = reverse(f'{self.api_url}:entry-service-owner-detail-api', kwargs={'pk': self.entry.pk})
        assert resolve(path).view_name == f'{self.api_url}:entry-service-owner-detail-api'
        assert resolve(path).kwargs == {'pk': str(self.entry.pk)}

    def test_api_entry_add_view(self):
        path = reverse(f'{self.api_url}:add-entry-to-cart-api', kwargs={'service_id': self.service.pk})
        assert resolve(path).view_name == f'{self.api_url}:add-entry-to-cart-api'
        assert resolve(path).kwargs == {'service_id': str(self.service.pk)}


