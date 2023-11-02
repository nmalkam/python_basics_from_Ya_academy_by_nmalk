import unittest
from unittest import mock

from C import news_announcement


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [25, 3, 'Начался саммит по глобальному потеплению',
                      'Завтра Новый год!',
                      'Python и Java конкурируют за звание самого популярного языка программирования']
        expected_output = ['Начался саммит по глоб...', 'Завтра Новый год!', 'Python и Java конкурир...']

        test_input2 = [6, 1, '12345']
        expected_output2 = '12345'
        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = news_announcement()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = news_announcement()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')


if __name__ == '__main__':
    unittest.main()
