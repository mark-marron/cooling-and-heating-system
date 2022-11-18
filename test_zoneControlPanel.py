import unittest
from zoneControlPanel import ZoneControl

z1 = ZoneControl
class Testset_temp(unittest.TestCase):
    def test_set_temp_type(self):
        #test set temp values of diff type
        self.assertRaises(TypeError, z1.set_target_temp, z1, 'q')

        self.assertRaises(TypeError, z1.set_target_temp, z1, 17.929)

        self.assertRaises(TypeError, z1.set_target_temp, z1, True)

        self.assertRaises(TypeError, z1.set_target_temp, z1, [8,9,0,3,5])

        self.assertRaises(TypeError, z1.set_target_temp, z1, {'key':'item'})

    def test_temp_values(self):
        #Test temp when temp values are of correct type but outside the range specified in interface.py
        z1.set_target_temp(z1,-6)
        self.assertAlmostEqual(z1.get_target_temp(z1), 0)

        z1.set_target_temp(z1,500)
        self.assertAlmostEqual(z1.get_target_temp(z1), 30)

        z1.set_target_temp(z1,4)
        self.assertAlmostEqual(z1.get_target_temp(z1), 4)

class Testset_timer(unittest.TestCase):
    def test_time_type(self):
        #Test time when values are of different type
        self.assertRaises(TypeError, z1.set_timer, z1, 'ewfewh')

        self.assertRaises(TypeError, z1.set_timer, z1, 2.989474)

        self.assertRaises(TypeError, z1.set_timer, z1, True)

        self.assertRaises(TypeError, z1.set_timer, z1, [6,7,8,9])

        self.assertRaises(TypeError, z1.set_timer, z1, {'key':'item'})

        self.assertRaises(ValueError, z1.set_timer, z1, -5)