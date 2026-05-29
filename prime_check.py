"""
## 3. Check if a Number is Prime

=================================================
PRIME NUMBER CHECK
=================================================

Problem Statement:
Write a Python program that takes a positive
integer as input and checks whether it is a
PRIME number.

A prime number is a natural number greater
than 1 that is divisible only by 1 and itself.

-------------------------------------------------
Instructions:
1. Take a positive integer n as input.
2. Use a for loop with range() to test possible
   divisors of n.

-------------------------------------------------
Input Example 1:
7

Output Example 1:
Prime

-------------------------------------------------
Input Example 2:
12

Output Example 2:
Not Prime

-------------------------------------------------
Explanation:
7 is divisible only by 1 and 7, so it is Prime.
12 is divisible by 2, 3, 4, 6, so it is Not Prime.
=================================================

"""
num = int(input("Enter a number: "))

count = 0

if num > 1:

    for i in range(1, num + 1):

        if num % i == 0:
            count = count + 1

    if count == 2:
        print(num, "is Prime Number")
    else:
        print(num, "is Not Prime Number")

else:
    print(num, "is Not Prime Number")