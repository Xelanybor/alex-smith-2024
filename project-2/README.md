# Question 2 - Weighted Sum Average

## Usage

From the project-2 directory, call:

```shell
python3 project2.py
```

The demo program generates a sine wave signal, and then uses a set of weights provided by the user to calculate the weighted sum average of the signal at multiple steps. The program will prompt you to enter the number of steps to run for, the step sizee, and the weights to use for the weighted sum average.

```shell
Question 2: Weighted Sum Average
=================================
This tool generates a sine wave to test the WeightedAverage class.
Enter the number of steps to generate the sine wave:
> 10
Enter the step size for the sine wave:
> 0.785
Enter the weights for the moving average filter, separated by spaces:
> 5 4 3 2 1
---------------------------------
Step | Sine | Weighted Sum Average
   1 | 0.00 | 0.00
   2 | 0.71 | 1.77
   3 | 1.00 | 2.61
   4 | 0.71 | 2.42
   5 | 0.00 | 1.45
   6 | -0.71 | 0.26
   7 | -1.00 | -1.08
   8 | -0.71 | -1.79
   9 | -0.00 | -1.45
  10 | 0.70 | -0.26
```

## Unit Tests

From the project-2 directory, call:

```shell
python3 tests.py
```