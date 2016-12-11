# String Basics

#### - String is a sequence of characters. 

#### - They are indexed starting with 0
    "hello"
     |||||
     01234

#### - We can access one character at a time using bracket operator as below:
    x = "hello"
    y = x[0] ########> gets 'h'

#### - We can create an empty string by assigning to an variable as below:
    x = ""
   
#### - We can use negative indices:
    "h  e  l  l  o"
     |  |  |  |  |
     0  1  2  3  4 --> positive indices
     |  |  |  |  |
    -5 -4 -3 -2 -1 --> negative indices

#### - Strings are immutable which means, you cannot do the below:
    x = "hello"
    x[0] = "j" # This is not allowed ####> will return TypeError: 'str' object
    does not support item assignment
    If we need to do something like that, we can try as below:
    x = "hello"
    x = "j" + x[1:] # by taking advantage of slice

#### - Slicing Strings (sub strings):
    "M O N T Y   P Y T H O N"
     | | | | | | | | | | | |
     0 1 2 3 4 5 6 7 8 9 10 11

    - Continous section of string using colon operator
      x = 'Monty Python' 
      x[0:4] = 'Mont'
    - The second number is one beyond the end of the slice
      'up to but not including'

#### - 'in' as a Operator:
    'a' in 'apple' = True
    'x' in 'apple' = False

#### - String Comparison:
    Operators:- '==' '>' '<'

#### - String Library:
    greet = 'Hello there!'
    greet.lower() - gives a lower case copy of greet but not change the variable
    dir() - gives different functions that are available for your disposal
    Ex: find(), strip(), startswith(), endswith()
