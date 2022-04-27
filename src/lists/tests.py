from django.urls import resolve
from django.test import TestCase
from lists.views import home_page


class HomePageTest(TestCase):
    """Тест домашней страницы"""

    def test_root_url_resolve_to_home_page_view(self):
        """Тест: корневой url преобразуется в представление домашней страницы"""
        found = resolve('/lists/')
        self.assertEqual(found.func, home_page)
