from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

UserModel = get_user_model()


class RegisterViewTest(TestCase):
    VALID_USER_DATA = {
        'username': 'valid_username',
        'password1': 'OPIG*H*)&FH@#$89fguwnrefgvj',
        'password2': 'OPIG*H*)&FH@#$89fguwnrefgvj',
        'email': 'test@test.test'
    }
    REGISTER_VIEW = reverse('register')

    def test_register__when_valid_data__expect_redirect_to_home_page(self):
        response = self.client.post(
            self.REGISTER_VIEW,
            data=self.VALID_USER_DATA
        )
        self.assertEqual(response.status_code, 302)  # Redirected Successfully

    def test_register__when_valid_data__expect_correctly_registered_user(self):
        # In order to use TEST DB instead of REAL DB, a Client() instance must be created before any other logic:
        # Either like this:
        # client = django.test.Client()
        # or if POST is needed (we need the interaction, not the return):
        self.client.post(
            self.REGISTER_VIEW,
            data=self.VALID_USER_DATA
        )

        user_exists = UserModel.objects \
            .filter(
            username=self.VALID_USER_DATA['username'],
            email=self.VALID_USER_DATA['email']
        ) \
            .exists()

        self.assertTrue(user_exists)

    def test_register__when_valid_data__expect_logged_in_user(self):
        # In order to use TEST DB instead of REAL DB, a Client() instance must be created before any other logic:
        # Either like this:
        # client = django.test.Client()
        # or if POST is needed (we need the interaction, not the return):
        self.client.post(
            self.REGISTER_VIEW,
            data=self.VALID_USER_DATA
        )

        user = UserModel.objects.get(username=self.VALID_USER_DATA['username'])
        user_logged_in = user.is_authenticated
        self.assertTrue(user_logged_in)

    def test_register__when_valid_data__expect_1_registered_user(self):
        self.client.post(
            self.REGISTER_VIEW,
            data=self.VALID_USER_DATA
        )
        users_count = UserModel.objects.count()
        self.assertEqual(users_count, 1)

    def test_registration_with_valid_data(self):  # ChatGPT help
        # client = Client()

        response = self.client.post(self.REGISTER_VIEW, data=self.VALID_USER_DATA)
        # self.assertEqual(response.status_code, 200)  # Assuming a successful registration returns a 200 status code

        # Check if the user is created in the test database
        objs = UserModel.objects.all()
        user_exists = UserModel.objects.filter(username=self.VALID_USER_DATA['username']).exists()
        self.assertTrue(user_exists)