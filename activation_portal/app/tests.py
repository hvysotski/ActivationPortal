import string
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from .models import Credentials, ActivationCode


class TodoListCreateAPIViewTestCase(APITestCase):

    def setUp(self):
        self.username = "admin2"
        self.password = "admin2"
        self.user = User.objects.create_user(self.username, self.password)
        self.token = self.user.auth_token
        self.api_authentication()
        self.credentials_data = dict(
            cea_login='login_cea',
            cea_password='password_cea',
            cima_login='login_cima',
            cima_password='password_cima',
        )

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_code_removal_after_get(self):

        credentials = Credentials.objects.create(**self.credentials_data)
        activation_code = credentials.activationcode.activation_code

        response = self.client.get(f'/codes/{activation_code}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.json(), dict(activation_code=activation_code, credentials=self.credentials_data))
        self.assertFalse(ActivationCode.objects.filter(activation_code=activation_code).exists())

    def test_get_not_authenticated(self):
        response = APIClient().get('/codes/asfad/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_activation_code_format(self):
        credentials = Credentials.objects.create(**self.credentials_data)
        activation_code = credentials.activationcode.activation_code
        for i in activation_code:
            if i in string.ascii_letters or string.digits:
                self.assertTrue(i)


