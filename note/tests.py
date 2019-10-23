from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from .models import Categories, Notes
from .utils import *


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
            text=encrypt('Test text', 'q1w2e3r4'),
            password='q1w2e3r4',
            category=self.category,
        )

    def test_invalid_note_new(self):
        self.c.login(username='testuser', password='secret')
        response = self.c.post(reverse('new_note', kwargs={'slug': self.category.slug}),
                               {'title': 'Test', 'text': 'Text', 'password': ''}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, "form", "password", "This field is required.")

    def test_string_representation(self):
        note = Notes(title='A sample title', password='q1w2e3r4')
        self.assertEqual(str(note), note.title)

    def test_note_get_absolute_url(self):
        self.assertEquals(self.note.get_absolute_url(), '/category/note/' + str(self.note.slug) + '/')

    def test_note_content(self):
        self.assertEqual(f'{self.note.title}', 'Test title')
        self.assertEqual(f'{self.note.category}', self.category.title)
        self.assertEqual(f'{decrypt(self.note.text, self.note.password)}', 'Test text')
        self.assertEqual(f'{self.note.password}', 'q1w2e3r4')

    def test_category_detail_view(self):
        self.c.login(username='testuser', password='secret')
        response = self.c.get('/category/note/' + str(self.note.slug) + '/')
        no_response = self.c.get('/category/note/vasvfrqafavrfvadvavdsv/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Test title')
        self.assertTemplateUsed(response, 'note/note_enterpsw.html')

    def test_note_create_view(self):
        self.c.login(username='testuser', password='secret')
        response = self.c.post(reverse('new_note', kwargs={'slug': self.category.slug}), {
            'title': 'New title',
            'text': 'New text',
            'password': 'a1s2d3f4'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')

    def test_note_detail_view(self):
        self.c.login(username='testuser', password='secret')
        response = self.c.post(reverse('note_detail', kwargs={'slug': self.note.slug}), {
                 'password': 'q1w2e3r4',
             },  follow=True)
        self.assertEqual(response.status_code, 200)

    def test_note_update_view(self):
        self.c.login(username='testuser', password='secret')
        response = self.c.post(reverse('note_edit', kwargs={'slug': self.note.slug}), {
            'title': 'Edit title',
            'text': 'Edit text',
            'password': 'zaxscdvf'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Edit text')

    def test_post_delete_view(self):
        self.c.login(username='testuser', password='secret')
        response = self.c.get(reverse('note_delete', kwargs={'slug': self.note.slug}))
        self.assertEqual(response.status_code, 200)
