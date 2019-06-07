from django.test import TestCase

from rest_framework.test import APITestCase, APIClient

from accounts.models import User


class BaseTestCaseMixin(object):
    """
    Create data that should be shared in all of our test cases
    """
    def setUp(self):
        # Create users for our test cases.
        self.admin_user = User.objects.create_superuser(
            'admin', 'testadmin@asdf.com', 'adminpassword')
        self.sally_user = User.objects.create_user('sally', 'sally@asdf.com',
                                                   '12345678')
        self.roger_user = User.objects.create_user('roger', 'roger@asdf.com',
                                                   '2424df22')


class BaseTestCase(BaseTestCaseMixin, TestCase):
    """
    Base test class for any non-API test cases. This is useful for testing
    functionality in models, utils, etc.
    """
    pass


class BaseAPITestCase(BaseTestCaseMixin, APITestCase):
    """
    Base test class for all of our API test cases. The main strategy should be
    to test each endpoint's methods and their expected results depending on the
    request that is sent.
    """
    def setUp(self):
        super(BaseAPITestCase, self).setUp()

        # Create api clients for our users
        self.admin_client = APIClient()
        self.admin_client.force_authenticate(self.admin_user)
        self.sally_client = APIClient()
        self.sally_client.force_authenticate(self.sally_user)
        self.roger_client = APIClient()
        self.roger_client.force_authenticate(self.roger_user)
