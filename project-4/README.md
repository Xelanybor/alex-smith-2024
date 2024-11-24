# Question 4: Number machine

## Usage

From the project-4 directory, call:

```shell
python3 project4.py
```

The demo program will prompt you to enter a number to be processed by the number machine. The number must be a 5-digit integer, otherwise the program will prompt you to enter a valid number.

```shell
Question 4: Number machine
=================================
Enter a 5-digit number:
> text
---------------------------------
Number must be an integer!
Enter a 5-digit number:
> 3.14
---------------------------------
Number must be an integer!
Enter a 5-digit number:
> 1234
---------------------------------
Number must have 5 digits!
Enter a 5-digit number:
> 123456
---------------------------------
Number must have 5 digits!
Enter a 5-digit number:
> 12345
=================================
Reversed number: 54321
Sum of digits: 15
Number with one added to each digit: 23456
```

## Testing

From the project-4 directory, call:

```shell
python3 tests.py
```