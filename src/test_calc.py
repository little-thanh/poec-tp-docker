import unittest
from calc import apply_vat

class TestAddMethods(unittest.TestCase):
    def test1(self):
        self.assertEqual(apply_vat(100,20), 120)

    def test2(self):
        self.assertEqual(apply_vat(55.25, 5.5), 58.28874999999999)

    def test3(self):
        self.assertEqual(apply_vat(0, 10), 0)

    def test4(self):
        self.assertEqual(apply_vat(-10.99, 10), 'Price (-10.99) is negative')

    def test5(self):
        self.assertEqual(apply_vat('wrong value', 10), 'Price (wrong value) is not a number')

    def test6(self):
        self.assertEqual(apply_vat(100, -10), 'Percent (-10) is negative')

    def test7(self):
        self.assertEqual(apply_vat(100, 110), 'Percent (110) is superior to 100%')

if __name__ == '__main__':
    unittest.main()
