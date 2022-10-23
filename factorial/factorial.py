def factorial(num):
    result = 1                      # give a variable the value of 1
    for i in range(1, num + 1):     # loop through the range of numbers starting from 1 till the number + 1, this is to make sure zero is not included. We basically saying start at 1 and end at the inputted number
        result *= i                 # update the value of result by multiplying the each numbers from the iteration with the next number till it gets to the last number
    print(result)                   # after multiplying all the numbers from the loop, we are to print out the updated value of result, which is the factorial of the number provided

factorial(6)                        # calling the function and also passing the parameter
