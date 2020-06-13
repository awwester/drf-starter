from django.urls import reverse

from core.tests import BaseAPITestCase


class AccountsAPITestCase(BaseAPITestCase):

    def test_user_can_login(self):
        url = reverse('jwt-create')
        payload = {
            "username": self.roger_user.username,
            "password": "2424df22"
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 200)
        expected = ['refresh', 'access']
        for key in expected:
            self.assertNotEqual(response.json().get(key), None)

    def test_user_can_refresh_credentials(self):
        url = reverse('jwt-create')
        payload = {
            "username": self.roger_user.username,
            "password": "2424df22"
        }
        response = self.client.post(url, payload)
        refresh_token = response.json().get('refresh')

        # Now that we have the token we can refresh.
        url = reverse('jwt-refresh')
        payload = {"refresh": refresh_token}
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json().get('access'), None)

    def test_incorrect_credentials(self):
        url = reverse('jwt-create')
        payload = {
            "username": self.roger_user.username,
            "password": "WRONGPASSWORD"
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 401)
        self.assertNotEqual(response.json().get('detail'), None)

    def test_user_can_register(self):
        url = reverse('user-list')
        payload = {
            "username": "newuser",
            "password": "somepassword1",
            "rePassword": "somepassword1",
            "firstName": "New",
            "lastName": "User",
            "email": "newuser@asdf.com",
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(response.json().get('email'), None)

    def test_user_can_get_their_data(self):
        url = reverse('user-me')
        response = self.roger_client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('email'), self.roger_user.email)
