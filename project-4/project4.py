class NumberMachine():
    """A class that represents a "Number Machine". A number machine accepts a five-digit number and transforms it in three ways, viz:
    - reverses the number. E.g. 12345 should be returned as 54321.
    - calculates the sum of its digits.
    - generates a new number by adding one to each of its digits. For example if the number that is input is 12391 then the output should be displayed as 23402.
    """

    # The number that is input into the number machine
    inputNumber = 0

    def __init__(self, number: int):
        """Create a new instance of the NumberMachine class.

        Args:
            number (int): The input number. Has to be a 5-digit integer.
        """
        pass

    def setNumber(self, number: int):
        """Set the input number of the number machine. The number must be a 5-digit integer.

        Args:
            number (int): Input number.
        """
        pass


    def reverseDigits(self) -> int:
        """Reverse the digits of the number.

        Returns:
            int: The input number with digits reversed.
        """
        pass

    def sumDigits(self) -> int:
        """Calculate the sum of the number's digits.

        Returns:
            int: The sum of the number's digits.
        """
        pass

    def addOne(self) -> int:
        """Generates a new number by adding one to each of its digits. For example if the number that is input is 12391 then the output should be displayed as 23402.

        Returns:
            int: The generated number.
        """
        pass