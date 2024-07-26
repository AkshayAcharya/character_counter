import unittest
from collections import Counter

def count_characters(s):
    return Counter(s)

class TestCountCharacters(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(count_characters(''), {})
        
    def test_single_character(self):
        self.assertEqual(count_characters('a'), {'a': 1})
        
    def test_multiple_characters(self):
        self.assertEqual(count_characters('akshayacharya'), {'a': 5, 'k': 1, 's': 1, 'h': 2, 'y': 2, 'c': 1, 'r': 1})
        
    def test_special_characters(self):
        self.assertEqual(count_characters('a!a!'), {'a': 2, '!': 2})
        
    def test_numbers_in_string(self):
        self.assertEqual(count_characters('8088699738'), {'8': 4, '0': 1, '6': 1, '9': 2, '7': 1, '3': 1})

if __name__ == '__main__':
    unittest.main()
