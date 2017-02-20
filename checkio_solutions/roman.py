#!/usr/local/bin/python

from sys import exit

"""
Numbers in this system are represented by combinations of letters from the
Latin alphabet.
Roman numerals, as used today, are based on seven symbols:
Symbol  I   V   X   L   C   D   M
Value   1   5   10  50  100 500 1,000
However, to avoid four characters being repeated in succession (such as IIII or
XXXX), subtractive notation is used:
Number  4   9   40  90  400 900
Notation    IV  IX  XL  XC  CD  CM
I placed before V or X indicates one less,so four is IV (one less than five)
and nine is IX (one less than ten)
X placed before L or C indicates ten less, so forty is XL (ten less than fifty)
and ninety is XC (ten less than a hundred)
C placed before D or M indicates a hundred less, so four hundred is CD
(a hundred less than five hundred) and nine hundred is CM
(a hundred less than a thousand)

Source: https://en.wikipedia.org/wiki/Roman_numerals
"""

# Digit Mapping
romanNumerals = ['M',
                 'CM',
                 'D',
                 'CD',
                 'C',
                 'XC',
                 'L',
                 'XL',
                 'X',
                 'IX',
                 'V',
                 'IV',
                 'I']

equivalentIntegers = [1000,
                      900,
                      500,
                      400,
                      100,
                      90,
                      50,
                      40,
                      10,
                      9,
                      5,
                      4,
                      1]

romanNumeralMap = zip(romanNumerals, equivalentIntegers)


def toRoman(n, debug=None):
    """convert integer to Roman numeral
    :rtype: str
    :param n: integer value to convert to roman numeral
    :param debug: prints debug statements
    :return: converted roman numeral
    """
    result = ""
    for numeral, integer in romanNumeralMap:
        if debug:
            print("Debug: Check if {} is greater than or equal to {}".format(
                n, integer))
        while n >= integer:
            if debug:
                print("Debug: Since {} is greater than or equal to {}".format(
                    n, integer))
                print("Debug: Append {} to the 'result', ".format(numeral) +
                      "which is now {} ".format(
                          '\'empty\'' if result == '' else result) +
                      "(Remember: {} is {})".format(numeral, integer))
            result += numeral
            if debug:
                print("Debug: Now the 'result' is {}".format(result))
                print("Debug: Subtract {} with {}".format(n, integer))
            n -= integer
            if debug:
                print("Debug: Now the value left to operate is {}".format(n))
    return result

if __name__ == '__main__':
    # Get info from the user
    try:
        number = input("Pick a number ranging from 1 to 3999: ")
        if isinstance(number, str):
            # Test to see if the string contains integer
            try:
                number = int(number)
            except ValueError:
                print("ERROR: {} is not an integer.".format(number))
                print("INFO: Please choose an integer and try again!")
                exit(1)
        # Test to see if integer value is recieved
        if not isinstance(number, int):
            print("ERROR: {} is not an integer.".format(number))
            print("INFO: Please choose an integer and try again!")
            exit(1)
        # Test to see if the given integer is within the desired range
        if not (0 < number < 4000):
            print("ERROR: {} is not in the range of 1 to 3999.".format(number))
            print("INFO: Choose appropriately and try again!")
            exit(1)
        debug_switch = raw_input(
            "Do you want to turn the debug ON to understand the logic?"
            "type (y)es (default: no): ")
        if debug_switch.strip() == '':
            debug_switch = False
        elif debug_switch.strip().lower().startswith('y'):
            debug_switch = True
        else:
            debug_switch = None
    except NameError:  # Catch NameError which can happen with bad user input
        print("ERROR: Invalid input.")
        print("INFO: Please choose an integer and try again!")
        exit(1)
    # Run conversion now
    roman_numeral = toRoman(int(number), debug=debug_switch)
    print("{} is converted as {} in roman numerals.".format(str(number),
                                                            roman_numeral))
