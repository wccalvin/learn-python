# Lambda Expressions

Lambda expressions allows us to create "anonymous" functions. This means we
can quickly create ad-hoc functions without properly defining a function
using def.

Lambda is less general than a properly defined def statement. It is limited
to a simple expression than a block of statements.

Lambda is designed for coding simple functions.

The best way to understand the syntax of the lambda function is to deduce it
from regular def functions as below.

Here's an example of how to square using regular def,

    ```
    def square(num):
        return num**2
    ```

Although not recommended, it can also be written as,

    ```
    def square(num): return num**2
    ```

This is how to write in lambda form,

    ```
    square = lambda num: num**2
    ```
