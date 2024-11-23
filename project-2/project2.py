from collections import deque

class WeightedAverage:
    """A class that processes inputs one at a time, and computes a weighted sum average using a set of weights, acting as a moving average filter.
    """

    def __init__(self, w: list[float]):
        """Create a new instance of WeightedAverage with a set of weights.
 
        Args:
             w (list[float]): The set of weights to be used as a sliding filter when processing inputs.
        """
        
        # Create a copy of the weights so that the weights can't be modified externally
        self.weights = w.copy() # Since the weights are floats, a shallow copy is fine

        # Create a deque to store the previous inputs
        self.previousInputs = deque(maxlen=len(w)) # With a max length, we don't need to manually remove elements when we have more elements than weights
  
    def process(self, x: float) -> float:
        """Process a single input from a list of values, and return the weighted average of the previous n inputs.
 
        For example, with weights `[5,4,3,2,1]`, previous inputs `[1,2,3,4]`, and a current input `5`, the weighted average of the last three inputs would be calculated as:
        ```
        y = (5*1 + 4*2 + 3*3 + 2*4 + 1*5) / 5 
          = 7.0
         ```
 
        Args:
            x (float): Single value input to be processed.
 
        Returns:
            float: The weighted average of previous inputs including the value currently being processed, using the set of weights that this instance of Weighted average was initialised with.
        """
        self.previousInputs.appendleft(x) # Append on the left so that the leftmost weight is applied to the most recent signal entry

        # Zip to get pairs of weights and entries, multiply each pair together, sum all of the products together, and then divide by how many entries there are.
        return sum([x*y for x, y in zip(self.weights, self.previousInputs)]) / len(self.previousInputs)