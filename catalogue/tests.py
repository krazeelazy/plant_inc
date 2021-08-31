from django.test import TestCase
from django.urls import reverse

from users.models import CustomUser

class FruitListViewTest(TestCase):
    def setUp(self):
        # Create two users
        test_user1 = CustomUser.objects.create_user(email='user3@test.com', password='testPassword')
        test_user2 = CustomUser.objects.create_user(email='user4@test.com', password='testPassword')
    
    #make sure users that aren't logged in are redirected to the login page if they try to access the fruit list
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('fruit-list'))
        self.assertRedirects(response, '/login/?next=/catalogue/fruit-list')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='user3@test.com', password='testPassword')
        response = self.client.get(reverse('fruit-list'))

        # Check our user is logged in
        self.assertEqual(login, True)

        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'catalogue/fruit_list.html')