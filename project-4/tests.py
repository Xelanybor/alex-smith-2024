import unittest

from project4 import NumberMachine

class TestNumberMachine(unittest.TestCase):

    def testConstructor(self):
        """Test the NumberMachine constructor.
        """

        with self.assertRaises(TypeError):
            NumberMachine("string") # test that it doesn't accept a string

        with self.assertRaises(TypeError):
            NumberMachine(3.14) # test that it doesn't accept a float
        
        with self.assertRaises(ValueError):
            NumberMachine(1234) # Test that it doesn't accept a number with fewer than 5 digits

        with self.assertRaises(ValueError):
            NumberMachine(123456) # Test that it doesn't accept a number with more than 5 digits

        machine = NumberMachine(12345) # Test that it does accept a 5 digit integer
        self.assertEqual(machine.inputNumber, 12345)
        self.assertListEqual(machine.digits, [1, 2, 3, 4, 5]) # Ensure the digits are split correctly

    def testSetNumber(self):
        """Test the setNumber method.
        """

        machine = NumberMachine(12345)

        with self.assertRaises(TypeError):
            machine.setNumber("string") # test that it doesn't accept a string

        with self.assertRaises(TypeError):
            machine.setNumber(3.14) # test that it doesn't accept a float
        
        with self.assertRaises(ValueError):
            machine.setNumber(1234) # Test that it doesn't accept a number with fewer than 5 digits

        with self.assertRaises(ValueError):
            machine.setNumber(123456) # Test that it doesn't accept a number with more than 5 digits

        machine.setNumber(54321) # Test that it does accept a 5 digit integer
        self.assertEqual(machine.inputNumber, 54321)
        self.assertListEqual(machine.digits, [5, 4, 3, 2, 1]) # Ensure the digits are split correctly

    def testReverseDigits(self):
        """Test the reverseDigits method.
        """

        machine = NumberMachine(12345)

        self.assertEqual(machine.reverseDigits(), 54321)

        machine.setNumber(56789)
        self.assertEqual(machine.reverseDigits, 98765)

    def testSumDigits(self):
        """Test the sumDigits method.
        """

        machine = NumberMachine(12345)

        self.assertEqual(machine.sumDigits(), 15)

        machine.setNumber(56789)
        self.assertEqual(machine.sumDigits(), 35)

    def testAddOne(self):
        """Test the addOne method.
        """

        machine = NumberMachine(12345)

        self.assertEqual(machine.addOne(), 23456)

        machine.setNumber(56789)
        self.assertEqual(machine.addOne(), 67890)

if __name__ == "__main__":
    unittest.main()