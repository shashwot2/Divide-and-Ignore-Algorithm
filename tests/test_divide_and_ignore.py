import unittest
from src.divide_and_ignore import divide_and_ignore

class TestDivideAndIgnore(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(divide_and_ignore([]), [])

    def test_single_element_list(self):
        self.assertEqual(divide_and_ignore([1]), [1])

    def test_multiple_elements_list(self):
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = divide_and_ignore(list)
        self.assertEqual(len(result), len(list) // 2)
        
    def test_list_with_duplicate_elements(self):
        list = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
        result = divide_and_ignore(list)
        self.assertEqual(len(result), len(list) // 2)

    def test_two_item_list(self):
        list = [1, 2]
        result = divide_and_ignore(list)
        self.assertEqual(len(result), 1)
        self.assertTrue(result[0] in list)

    def test_list_with_different_types(self):
        list = [1, 'a', 3.14, [1, 2, 3]]
        result = divide_and_ignore(list)
        self.assertEqual(len(result), len(list) // 2)

if __name__ == '__main__':
    unittest.main()