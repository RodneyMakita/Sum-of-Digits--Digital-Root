Function Definition:

We define a function called digital_root that takes one argument, n, representing the non-negative integer whose digital root we want to find.
While Loop:

We use a while loop to repeatedly perform the digital root calculation until we obtain a single-digit number. The loop continues as long as the value of n is greater than or equal to 10.
Digit Sum Calculation:

Inside the loop, we convert the integer n into a string using str(n). Then we iterate through each character (which represents a digit) in the string, convert it back to an integer using int(digit), and sum these integers using the sum() function.
This calculates the sum of the digits of n.
Updating n:

We update the value of n to be the sum calculated in the previous step.
Returning the Result:

Once the value of n becomes less than 10 (i.e., it's a single-digit number), the loop exits, and we return the value of n as the digital root of the original input number.
Example Usage:

We prompt the user to enter a non-negative integer using input(), convert it to an integer using int(), and store it in the variable number.
We then call the digital_root function with the number as an argument and store the result in the variable result.
Finally, we print the original number and its digital root.
This code calculates the digital root of a given non-negative integer following the specified algorithm.

```python
def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Example usage:
number=int(input('Input Your Number My Dear LEGEND: '))
result=digital_root(number)
print("Your Input is: ",number,"\nYour Output Is: ",result)

