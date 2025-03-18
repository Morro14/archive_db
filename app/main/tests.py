from django.test import TestCase, Client
from .models import MyUser

# Create your tests here.


class UserAddTest(TestCase):
    def test_group_add(self):
        user = MyUser.objects.create(email="test@email.com", username="test_user")
