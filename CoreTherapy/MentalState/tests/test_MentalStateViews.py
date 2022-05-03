from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from CoreTherapy.MentalState.views import MentalStateViewSet



class TestUser(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view = MentalStateViewSet.as_view({'get': 'list'})
        self.uri = '/mentalstate/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()


    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            username ='test',
            email = 'testuser@test.com',
            password = 'test'
            )
    

    
    def test_list(self):
        request = self.factory.get(self.uri,
            HTTPP_AUTHORIZATION = 'Token {}'.format(self.token.key)
                                   )
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code)
                         )


    def test_list2(self):
        self.client.login(username="test", email="testuser@test.com", password="test")
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code)
                         )

    def test_create(self):
        self.client.login(username="test", email="testuser@test.com", password="test")
        params = {
            'candidate' : {
                 'username':'test1',
                 'email': 'test1user@test.com',
                 'password': 'test1'
                },
            'therapist': {
                 'username': 'test2',
                 'email': 'test2user@test.com',
                 'password': 'test2'
                },
            'candidates_note':'Feeling fantastic today, all is possible.',
            }
        response = self.client.post(self.uri, params, format="json")
        self.assertEqual(response.status_code, 201,
                        'Expected Response Code 201, received {0} instead.'
                        .format(response.status_code)
                        )
