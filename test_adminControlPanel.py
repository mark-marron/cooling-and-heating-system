import unittest
from adminControlPanel import AdminControl

a1 = AdminControl

"""
This test suite is for testing the methods that the user has the ability to interact with in adminControl Panel.py.
These methods include: set_target_temp/get_target_temp and set_timer.
2 different classes are made as the target temperature and the timer both have their own entry box to which the user can input values.
For other such methods the users does not input any value for example in the case of the room selection, the user picks from a predefined list so it is safe to assume 
-these variables do not cause errors.
A number of different test will be ran in these test classes as precaution for if the user input is invalid - for example they input a string instead of an integer and so on.

For test_temp_type we use assertRaises to check is a type error is raised for the scenarios when a user inputs a value of a type that is not integer.
For test_temp_values we assume the user has input the correct type but that the value they entered may be out of the specified range.
This is done through the use of assertAlmostEqual to see when the function is ran with an input if it gives the expected output 
- which in our case is: if the input is below 0, 0 is displayer, if the value is above 30, 30 is displayed and any value in between is displayed as is.


For test_time_type once again we use assertRaises to check if a type error is raise for the scenarios where a user input is not of type int.
We also have a Value error raised for once instance: this is where the user inputs a negative value for time.
The reasoning for throwing a valueError instead of using assertAlmostEqual is because it is not possible for time to be a negative value whereas temperature can.

In test_temp_type 6 test scenarios are ran to check if TypeErrors are raised.
In test_temp_values 3 test scenarios are ran to check if the actual output is almost equal(within 7 decimal places) to the expected output.

In test_time_type 6 test scenarios are ran to check if TypeErrors are raised.
In test_time_type 1 test scenario is ran to check if a ValueError is raised.
"""

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
