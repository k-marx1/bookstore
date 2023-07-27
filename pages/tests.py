from django.test import SimpleTestCase
from django.urls import reverse, resolve

from pages.views import HomePageView


class HomepageTests(SimpleTestCase):
    def setUp(self) -> None:
        url = reverse('pages:home')
        self.response = self.client.get(url)


    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_does_contains_incorrect_html(self):

        self.assertContains(self.response, 'Home page')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Aboba')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
