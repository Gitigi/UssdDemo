from django.test import TestCase
from core.models import Customer
import re

class InitialScreenTest(TestCase):
    def get_screen(self):
        return self.client.get("/ussd-endpoint",{'phoneNumber':self.phoneNumber,
                                                     'sessionId':self.sessionId,
                                                     'text':self.text})
    def setUp(self):
        self.phoneNumber = "34343408"
        self.sessionId = "dfdfdf"
        self.text = ''

    def test_initial_screen(self):
        screen = self.get_screen()
        self.assertEqual('Home\n1. My Account\n2. Product And Services\n',screen.content.decode())

    def test_my_account_screen(self):
        self.sessionId = '343434'
        self.get_screen()
        self.text = "1"
        response = self.get_screen()
        self.assertEqual('Account\n1. Balance\n2. Top up\n',response.content.decode())

    def test_my_account_balance_screen(self):
        self.sessionId = '3434ffd'
        self.get_screen()
        self.text = "1"
        self.get_screen()
        response = self.get_screen()
        self.assertRegex(response.content.decode(),'Your balance is ([0-9]+(.[0-9]+)?)')

    def test_my_account_top_up_screen(self):
        self.sessionId = '34weffd'
        self.get_screen()
        self.text = "1"
        self.get_screen()
        self.text='2'
        response = self.get_screen()
        self.assertContains(response,'Choose your domination')
        response = self.get_screen()
        self.assertRegex(response.content.decode(),'Top Successful bought ([0-9]+) units. New Balance is ([0-9]+)')

    def test_product_and_serices_screen(self):
        self.sessionId = 'dfdfdfd'
        self.get_screen()
        self.text='2'
        response = self.get_screen()
        self.assertEqual('Product And Services\n1. Dictionary\n',response.content.decode())
