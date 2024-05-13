import unittest
from main import get_valid_index

class TestMain(unittest.TestCase):
    def setup(self):
        pass 
    
    def test_get_valid_index(self):
        # 'get_valid_index' fonksiyonunun doğru sonuç verip vermediğini test ediyoruz
        self.assertEqual(get_valid_index(5, 'Bir sayı girin (3 girmen gerekli, list index karsiligi 2): '), 2)
    
    def test_get_valid_index_not_equal(self):
        # 'get_valid_index' fonksiyonunun yanlış sonuç verip vermediğini test ediyoruz
        self.assertNotEqual(get_valid_index(5, 'Bir sayı girin (3 girmen gerekli, list index karsiligi 2): '), 3)
if __name__ == '__main__':
    unittest.main()