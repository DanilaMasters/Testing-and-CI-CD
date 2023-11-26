import unittest

from prime import is_prime

class Tests(unittest.TestCase):

    def test_1(self):
        return self.assertFalse(is_prime(1))
    
    def test_2(self):
        return self.assertTrue(is_prime(2))
    
    def test_8(self):
        return self.assertFalse(is_prime(8))
    
    def test_11(self):
        return self.assertTrue(is_prime(11))
    
    def test_25(self):
        return self.assertFalse(is_prime(25))

    def test_28(self):
        return self.assertFalse(is_prime(28))


if __name__ == "__main__":
    unittest.main()