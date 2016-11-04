#!/usr/bin/env python

addition = lambda num1, num2: num1 + num2
multiplication = lambda num1, num2: num1 * num2

# Check if the number is even using lambda expression
even = lambda num: num % 2 == 0

# Reverse a string using lambda expressions
rev = lambda s: s[::-1]


if __name__ == '__main__':
    print multiplication(2, 4)
    print addition(2, 4)
    print even(10)
    print even(11)
    print rev('Clayton')
