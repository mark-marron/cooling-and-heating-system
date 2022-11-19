import unittest
from adminControlPanel import AdminControl

a1 = AdminControl


class TestsetTargetTemp(unittest.TestCase):
    def test_temp_type(self):
        # Test temp when values are of different type
        self.assertRaises(TypeError, a1.set_target_temp, a1, 'q')

        self.assertRaises(TypeError, a1.set_target_temp, a1, 17.929)

        self.assertRaises(TypeError, a1.set_target_temp, a1, True)

        self.assertRaises(TypeError, a1.set_target_temp, a1, [8, 9, 0, 3, 5])

        self.assertRaises(TypeError, a1.set_target_temp, a1, {'key': 'item'})

        self.assertRaises(TypeError, a1.set_target_temp, a1, 5.79J)

    def test_temp_values(self):
        # Test temp when temp values are of correct type but outside the range specified in interface.py
        a1.set_target_temp(a1, -6)
        self.assertAlmostEqual(a1.get_target_temp(a1), 0)

        a1.set_target_temp(a1, 500)
        self.assertAlmostEqual(a1.get_target_temp(a1), 30)

        a1.set_target_temp(a1, 4)
        self.assertAlmostEqual(a1.get_target_temp(a1), 4)


class TestsetTimer(unittest.TestCase):
    def test_time_type(self):
        # Test time when values are of different type
        self.assertRaises(TypeError, a1.set_timer, a1, 'ewfewh')

        self.assertRaises(TypeError, a1.set_timer, a1, 2.989474)

        self.assertRaises(TypeError, a1.set_timer, a1, True)

        self.assertRaises(TypeError, a1.set_timer, a1, [6, 7, 8, 9])

        self.assertRaises(TypeError, a1.set_timer, a1, {'key': 'item'})

        self.assertRaises(ValueError, a1.set_timer, a1, -5)

        self.assertRaises(TypeError, a1.set_timer, a1, 5.79J)
