import unittest
from zoneControlPanel import ZoneControl

z1 = ZoneControl

"""
This test suite is for testing the methods that the user has the ability to interact with in zoneControlPanel.py.
These methods include: set_target_temp/get_target_temp and set_timer.
2 different classes are made as the target temperature and the timer both have their own entry box to which the user can input values.
For other such methods the users does not input any value for example the other methods in zoneControlPanel are getters which only return a value but do not 
-input a value meaning by this stage an errors that might be received should have been caught in the setters.
A number of different test will be ran in these test classes as precaution for if the user input is invalid - for example they input a string instead of an integer and so on.

For test_set__temp_type we use assertRaises to check is a type error is raised for the scenarios when a user inputs a value of a type that is not integer.
For test_temp_values we assume the user has input the correct type but that the value they entered may be out of the specified range.
This is done through the use of assertAlmostEqual to see when the function is ran with an input if it gives the expected output 
- which in our case is: if the input is below 0, 0 is displayer, if the value is above 30, 30 is displayed and any value in between is displayed as is.


For test_time_type once again we use assertRaises to check if a type error is raise for the scenarios where a user input is not of type int.
We also have a Value error raised for once instance: this is where the user inputs a negative value for time.
The reasoning for throwing a valueError instead of using assertAlmostEqual is because it is not possible for time to be a negative value whereas temperature can

In comparison to the test_adminControlPanel instead of the methods being called from the adminControlPanel they are called from the zoneControlPanel 
-to stick to what was outlined in the sequence diagrams.

In test_set_temp_type 6 test scenarios are ran to check if TypeErrors are raised.
In test_temp_values 3 test scenarios are ran to check if the actual output is almost equal(within 7 decimal places) to the expected output.

In test_time_type 6 test scenarios are ran to check if TypeErrors are raised.
In test_time_type 1 test scenario is ran to check if a ValueError is raised.
"""

class TestsetTemp(unittest.TestCase):
    def test_set_temp_type(self):
        # test set temp values of diff type
        self.assertRaises(TypeError, z1.set_target_temp, z1, 'q')

        self.assertRaises(TypeError, z1.set_target_temp, z1, 17.929)

        self.assertRaises(TypeError, z1.set_target_temp, z1, True)

        self.assertRaises(TypeError, z1.set_target_temp, z1, [8, 9, 0, 3, 5])

        self.assertRaises(TypeError, z1.set_target_temp, z1, {'key': 'item'})

        self.assertRaises(TypeError, z1.set_target_temp, z1, 7.41J)

    def test_temp_values(self):
        # Test temp when temp values are of correct type but outside the range specified in interface.py
        z1.set_target_temp(z1, -6)
        self.assertAlmostEqual(z1.get_target_temp(z1), 0)

        z1.set_target_temp(z1, 500)
        self.assertAlmostEqual(z1.get_target_temp(z1), 30)

        z1.set_target_temp(z1, 4)
        self.assertAlmostEqual(z1.get_target_temp(z1), 4)


class TestsetTimer(unittest.TestCase):
    def test_time_type(self):
        # Test time when values are of different type
        self.assertRaises(TypeError, z1.set_timer, z1, 'ewfewh')

        self.assertRaises(TypeError, z1.set_timer, z1, 2.989474)

        self.assertRaises(TypeError, z1.set_timer, z1, True)

        self.assertRaises(TypeError, z1.set_timer, z1, [6, 7, 8, 9])

        self.assertRaises(TypeError, z1.set_timer, z1, {'key': 'item'})

        self.assertRaises(ValueError, z1.set_timer, z1, -5)

        self.assertRaises(TypeError, z1.set_timer, z1, 5.79J)
