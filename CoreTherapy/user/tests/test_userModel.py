import json
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

class UserRegistrationAPIViewTestCase(APITestCase):
    url = reverse("users")

    def test_invalid_password(self):
        """
        Test to verify that a post call with invalid password
        """
        user_data = {
            "username": "testuser",
            "email": "test@testuser.com",
            "password":"password",
            "confirm_password": "INVALID_PASSWORD"
            }
        response = self.client.post(self.url, user_data, format="json")
        self.assertEqual(400, response.status_code)
        

    def test_user_registration(self):
        """
        Test to verify that a post call with a use valid data
        """
        user_data = {
            "username": "testuser",
            "email": "test@testuser.com",
            "password": "123123",
            "confirm_password": "123123"
            
            }
        response = self.client.post(self.url, user_data)
        self.asserEqual(201, response.status_code)
        self.assertTrue("token" in json.loads(response.content))

    def test_unique_username_validation(self):
        """
        Test to verify that a post call with already exists username
        """
        user_data_1 = {
            "username": "testuser",
            "email": "test@testuser.com",
            "password": "123123",
            "confirm_password": "123123"
            }
        response = self.client.post(self.url, user_data_1, format="json")
        self.asserEqual(201, response.status_code)

        user_data_2 = {
            "username": "testuser",
            "email": "test2@testuser.com",
            "password": "123123",
            "confirm_password": "123123",
            }

class UserTokenAPIViewTestCase(APITestCase):
    def url(self, key):
        return reverse("api/token : api-token")

    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

        self.user_2 = User.objects.create_user("mary", "mary@earth.com", "super_secret")
        self.token_2 = Token.objects.create(user=self.user_2)


    def tearDown(self):
        self.user.delete()
        self.token.delete()
        self.user_2.delete()
        self.token_2.delete()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_delete_by_key(self):
        response = self.client.delete(self.url(self.token.key))
        self.assertEqual(204, response.status_code)
        self.asserFalse(Token.objects.filter(key=self.token.key).exists())

    def test_delete_current(self):
        response = self.client.delete(self.url('current'))
        self.assertEqual(204, response.status_code)
        self.assertFalse(Token.objects.filter(key=self.token.key).exists())

    def test_delete_unauthorized(self):
        response = self.client.delete(self.url(self.token_2.key))
        self.assertEqual(404, reponse.status_code)
        self.assertTrue(Token.objects.filter(key=self.token_2.key).exists())

    def test_get(self):
        #Test that unauthorized access return 404
        response = self.client.get(self.url(key))
        self.assertEqual(200, response.status_code)
        for key in [self.token.key, 'current']:
            response = self.client.get(self.url(key))
            self.assertEqual(200, response.status_code)
            self.assertEqual(self.token.key, response.data['auth_token'])
            self.assertIn('created', response.data)
