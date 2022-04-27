from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitor(unittest.TestCase):

    def setUp(self) -> None:
        """Установка"""
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Тест: можно начать список и получить его позже"""
        # Открываем страницу
        self.browser.get('http://0.0.0.0:8010')

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item',
        )

        # Вводим текст - 'Купить павлиньи перья'
        inputbox.send_keys('Купить павлиньи перья')
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Купить павлиньи перья' for row in rows)
        )
        # текстовое поле приглашает еще ввести текст
        # Вводим 'сделать мушку из павлиньих перьев'
        self.fail('закончить тест')

        # Страница снова обновляется и теперь показывает оба элемента ее списка

