from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from .models import Categories, Notes


class CategoryTests(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',

        )
        self.category = Categories.objects.create(
            title='A good title',
            user=self.user,
        )
        self.note = Notes.objects.create(
            title='Test title',
            text='Test text',
            password='q1w2e3r4',
            category=self.category,

        )

    def test_category_login(self):
        response = self.c.get(reverse('home'))
        print(response.status_code)
        self.assertEqual(response.status_code, 302)

        self.c.login(username='testuser', password='secret')
        response = self.c.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_invalid_note_new(self):
        self.c.login(username='testuser', password='secret')
        response = self.c.post(reverse('new_note', kwargs={'slug': self.category.slug}),
                               {'title': 'Test', 'text': 'Text', 'password': ''}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, "form", "password", "This field is required.")

    def test_string_representation(self):
        note = Notes(title='A sample title', password='q1w2e3r4')
        self.assertEqual(str(note), note.title)

    def test_category_get_absolute_url(self):
        self.assertEquals(self.note.get_absolute_url(), '/category/note/' + str(self.note.slug) + '/')

    def test_category_content(self):
        self.assertEqual(f'{self.note.title}', 'Test title')
        self.assertEqual(f'{self.note.category}', self.category.title)
        self.assertEqual(f'{self.note.text}', 'Test text')
        self.assertEqual(f'{self.note.password}', 'q1w2e3r4')

    # def test_category_detail_view(self):
    #     self.c.login(username='testuser', password='secret')
    #     response = self.c.get('/category/note/' + str(self.note.slug) + '/')
    #     no_response = self.c.get('/category/note/vasvfrqafavrfvadvavdsv/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(no_response.status_code, 404)
    #     self.assertContains(response, 'Test title')
    #     self.assertTemplateUsed(response, 'note/note_enterpsw.html')
    #     response = self.c.post(reverse('note_detail', kwargs={'slug': self.note.slug}), {
    #         'password': 'q1w2e3r4',
    #     },  follow=True)
    #     self.assertEqual(response.status_code, 200)

    def test_category_create_view(self):
        self.c.login(username='testuser', password='secret')
        response = self.c.post(reverse('new_category'), {
            'title': 'New title',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
