import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests for class Employee"""

    def setUp(self):
        """Create """
        self.first = "Liudmyla"
        self.last = "Yasinkovska"
        self.salary = 10000
        self.me = Employee(self.first, self.last, self.salary)


    def test_give_default_raise(self):
        self.me.give_raise()
        self.assertEqual(self.me.salary, 15000)


    def test_give_custom_raise(self):
        self.me.give_raise(9000)
        self.assertEqual(self.me.salary, 19000)
