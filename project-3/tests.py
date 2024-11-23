import unittest

from project3 import isPangram

class TestIsPangram(unittest.TestCase):

    def testIsPangram(self):
        """Test the isPangram method with know pangrams.
        """

        # Tests with regular english alphabet
        self.assertTrue(isPangram('abcdefghijklmnopqrstuvwxyz')) # the whole alphabet, definitely a pangram
        self.assertTrue(isPangram('The quick brown fox jumps over the lazy dog')) # well-known

        self.assertFalse(isPangram(''))
        self.assertFalse(isPangram('abcdefghijklmnopqrstuvwxyy')) # missing z

        # Tests with different alphabets
        self.assertFalse(isPangram('The quick brown fox jumps over the lazy dog', alphabet='abcdefghijklmnopqrstuvwxyz@')) # alphabet contains the @ symbol, which is not in the string
        self.assertTrue(isPangram('abc', alphabet='abc')) # with a smaller alphabet

if __name__ == "__main__":
    unittest.main()