class NumberMachine():
    """A class that represents a "Number Machine". A number machine accepts a five-digit number and transforms it in three ways, viz:
    - reverses the number. E.g. 12345 should be returned as 54321.
    - calculates the sum of its digits.
    - generates a new number by adding one to each of its digits. For example if the number that is input is 12391 then the output should be displayed as 23402.
    """

    def __init__(self, number: int):
        """Create a new instance of the NumberMachine class.

        Args:
            number (int): The input number. Has to be a 5-digit integer.

        Raises:
            TypeError: Raised if the input number is not an integer.
            ValueError: Raised if the input number is not 5 digits.
        """
        self.setNumber(number)

    def setNumber(self, number: int):
        """Set the input number of the number machine. The number must be a 5-digit integer.

        Args:
            number (int): Input number.

        Raises:
            TypeError: Raised if the input number is not an integer.
            ValueError: Raised if the input number is not 5 digits.
        """
        
        # Make sure the number is an int
        if type(number) != int:
            raise TypeError
        
        # make sure the number is 5 digits
        if number < 10000 or number > 99999:
            raise ValueError
        
        # Set the input number
        self.inputNumber = number

        # Set the digits of the number (this makes later calculations easier and this way we only do it once)
        self.digits = [0] * 5
        for i in range(4, -1, -1): # Set the digits in reverse order, from ones up to ten thousands
            self.digits[i] = number % 10 # Get the smallest digit
            number //= 10



    def reverseDigits(self) -> int:
        """Reverse the digits of the number.

        Returns:
            int: The input number with digits reversed.
        """
        # I came up with the cool one-liner but it's not very readable so I'm not using it
        # But I think it looks cool so I'm leaving it in
        # return sum([x * 10 ** i for i, x in enumerate(self.digits)])

        reversedNumber = 0 # the number to be returned

        # Loop through the digits of the input number
        for i in range(5):
            # To get a digit in position i into its new position, we multiply it by 10^i
            # For example, a digit in position 0 of a 5-digit number is actually multiplied 10^4
            # e.g. (1)2345 => in 1x10^4
            # When reversed, this digit must go into position (4-0) = 4, where it must be multiplied by 10^0
            # i.e. 5432(1) => 1x10^0
            reversedNumber += self.digits[i] * 10 ** i

        return reversedNumber


    def sumDigits(self) -> int:
        """Calculate the sum of the number's digits.

        Returns:
            int: The sum of the number's digits.
        """
        return sum(self.digits)

    def addOne(self) -> int:
        """Generates a new number by adding one to each of its digits. For example if the number that is input is 12391 then the output should be displayed as 23402.

        Returns:
            int: The generated number.
        """
        sumOneNumber = 0 # the number to be returned

        # Loop through the digits of the input number
        for i in range(5):
            powerOf10 = 10 ** (4 - i) # As in reverseNumber(), a digit is put in position n by multiplying by 10^(4-n)
            newDigit = (self.digits[i] + 1) % 10 # Increment the digit by 1, and mod so 10 becomes 0 again
            sumOneNumber += newDigit * powerOf10

        return sumOneNumber
    
if __name__ == "__main__":
    # CLI to demonstrate usage of the class
    print("Question 4: Number machine")
    print("=================================")

    numberMachine = None

    while not numberMachine:

        number = input("Enter a 5-digit number:\n> ")
        try:
            number = int(number) # Make sure the input is an integer
        except ValueError:
            print("---------------------------------")
            print("Number must be an integer!")
            continue

        try:
            numberMachine = NumberMachine(number)
        except ValueError:
            print("---------------------------------")
            print("Number must have 5 digits!") # Make sure the number is 5 digits
        except TypeError:
            print("---------------------------------")
            print("Number must be an integer!") # Make sure the number is an integer

    print("=================================")
    print(f"Reversed number: {numberMachine.reverseDigits()}")
    print(f"Sum of digits: {numberMachine.sumDigits()}")
    print(f"Number with one added to each digit: {numberMachine.addOne()}")