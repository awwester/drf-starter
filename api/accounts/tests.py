from django.urls import reverse

from core.tests import BaseAPITestCase



class AccountsAPITestCase(BaseAPITestCase):

    def test_user_can_login(self):
        url = reverse('rest_login')
        payload = {
            "username": self.roger_user.username,
            "password": "2424df22"
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 200)

    def test_incorrect_credentials(self):
        url = reverse('rest_login')
        payload = {
            "username": self.roger_user.username,
            "password": "WRONGPASSWORD"
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 400)

    def test_user_can_logout(self):
        url = reverse('rest_logout')
        response = self.roger_client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_user_can_register(self):
        url = reverse('rest_register')
        payload = {
            "username": "newuser",
            "password1": "somepassword1",
            "password2": "somepassword1",
            "firstName": "New",
            "lastName": "User",
            "email": "newuser@asdf.com",
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(response.json().get('key'), None)

    def test_user_can_get_their_data(self):
        url = reverse('user-me')
        response = self.roger_client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('email'), self.roger_user.email)
