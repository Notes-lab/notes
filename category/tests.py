from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from .models import Categories


class CategoryTests(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.category = Categories.objects.create(
            title='A good title',
            user=self.user,
        )

    def test_category_login(self):
        response = self.c.get(reverse('home'))
        self.assertEqual(response.status_code, 302)

        self.c.login(username='testuser', password='secret')
        response = self.c.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_invalid_category_new(self):
        self.c.login(username='testuser', password='secret')
        response = self.c.post(reverse('new_category'),
                               {'title': ''}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, "form", "title", "This field is required.")

    def test_string_representation(self):
        category = Categories(title='A sample title')
        self.assertEqual(str(category), category.title)

    def test_category_get_absolute_url(self):
        self.assertEquals(self.category.get_absolute_url(), '/category/')

    def test_category_content(self):
        self.assertEqual(f'{self.category.title}', 'A good title')
        self.assertEqual(f'{self.category.user}', 'testuser')

    def test_category_detail_view(self):
        self.c.login(username='testuser', password='secret')
        response = self.c.get('/category/')
        no_response = self.c.get('/category/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'category/home.html')

    def test_category_create_view(self):
        self.c.login(username='testuser', password='secret')
        response = self.c.post(reverse('new_category'), {
            'title': 'New title',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
