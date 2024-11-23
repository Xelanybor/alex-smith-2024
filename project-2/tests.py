import unittest

from project2 import WeightedAverage

class TestWeightedAverage(unittest.TestCase):

    def testWeightedAverage(self):
        """Test that the weighted average is calculated correctly."""

        # Create a new instance of WeightedAverage with a set of weights
        weights = [5,4,3,2,1]
        weightedAverage = WeightedAverage(weights)

        # Test that the weighted average is calculated correctly
        self.assertEqual(weightedAverage.process(5), 25) # (5*5) / 1 = 25
        self.assertEqual(weightedAverage.process(4), 20) # (5*4 + 4*5) / 2 = 20
        self.assertEqual(weightedAverage.process(3), 46/3) # (5*3 + 4*4 + 3*5) / 3 = 46/3
        self.assertEqual(weightedAverage.process(2), 11) # (5*2 + 4*3 + 3*4 + 2*5) / 4 = 11
        self.assertEqual(weightedAverage.process(1), 7) # (5*1 + 4*2 + 3*3 + 2*4 + 1*5) / 5 = 7

if __name__ == "__main__":
    unittest.main()