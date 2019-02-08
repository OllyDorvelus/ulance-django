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
        cls.user3 = mixer.blend(User, username='username3')
        cls.order = mixer.blend('orders.ServiceOrderModel', buyer=cls.user, paid=4.99)
        cls.cart = mixer.blend('orders.CartModel', user=cls.user, item_count=0)
        cls.cart2 = mixer.blend('orders.CartModel', user=cls.user2)
        cls.service = mixer.blend('services.ServiceModel', price=5.00, user=cls.user, name='service_name')
        cls.service2 = mixer.blend('services.ServiceModel', price=10.00, user=cls.user, name='service_name2', description='aaaa')
        cls.entry = mixer.blend('orders.EntryModel', cart=cls.cart2, quantity=2, service=cls.service)
        cls.entry2 = mixer.blend('orders.EntryModel', cart=cls.cart2, quantity=3, service=cls.service2)
        cls.order_entry = mixer.blend('orders.EntryModel', order=cls.order, service=cls.service)
        cls.complaint = mixer.blend('orders.ComplaintModel', reason='some reason', entry=cls.order_entry, status='INP')

    def test_order_to_string(self):
        assert str(self.order) == 'username - $4.99'

    def test_order_get_total(self):
        pass

    def test_cart_to_string(self):
        assert str(self.cart) == 'username - 0'

    def get_total_for_no_items_in_cart(self):
        assert self.cart.get_total() == 0

    def get_total_for_items_in_cart(self):
        assert self.cart2.get_total() == 40.00

    def get_count_for_no_items_in_cart(self):
        assert self.cart.get_count() == 0

    def get_count_for_items_in_cart(self):
        assert self.cart2.get_count() == 5

    def test_clear_all_cart_entries(self):
        new_cart = mixer.blend('orders.CartModel', user=self.user3)
        self.new_entry = mixer.blend('orders.Entrymodel', service=self.service, quantity=2, cart=new_cart)
        self.new_entry2 = mixer.blend('orders.Entrymodel', service=self.service2, quantity=2, cart=new_cart)
        new_cart.clear_cart()
        assert new_cart.item_count == 0
        assert new_cart.total == 0
        assert new_cart.cart_entries.count() == 0

    def delete_all_cart_entries(self):
        new_cart = mixer.blend('orders.CartModel', user=self.user3)
        self.new_entry = mixer.blend('orders.Entrymodel', service=self.service, quantity=2, cart=new_cart)
        self.new_entry2 = mixer.blend('orders.Entrymodel', service=self.service2, quantity=2, cart=new_cart)
        new_cart.remove_all_entries()
        assert new_cart.item_count == 0
        assert new_cart.total == 0
        assert new_cart.cart_entries.count() == 0

    def test_entry_in_cart_to_string(self):
        assert str(self.entry) == 'username | service_name requested by username2'

    def test_entry_in_order_to_string(self):
        assert str(self.order_entry) == 'username | service_name requested by username'

    def test_complaint_to_string(self):
        assert str(self.complaint) == 'username - some reason'

    def test_no_complaint_if_entry_not_complete(self):
        self.assertRaises(ValidationError, self.complaint.clean)

    # def test_entry_cant_be_order_and_in_cart(self):
    #     new_cart = mixer.blend('orders.CartModel', user=self.user3)
    #     new_entry = mixer.blend('orders.EntryModel', order=self.order, cart=new_cart, service=self.service2)
    #     self.assertRaises(ValidationError, new_entry.clean)
    #
    # def test_entry_cant_be_not_ordered_and_have_status(self):
    #     new_user = mixer.blend(User, username='some_user')
    #     new_cart2 = mixer.blend('orders.CartModel', user=new_user)
    #     new_entry2 = mixer.blend('orders.EntryModel', cart=new_cart2, service=self.service2, is_ordered=True, status='COM')
    #     self.assertRaises(ValidationError, new_entry2.clean())


