#!/usr/local/bin/python3


def three_words(words):
    n = 0
    split_words = words.split()
    for word in split_words:
        if word.isalpha():
            n += 1
        else:
            n = 0
        if n == 3:
            return True
    return False


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert three_words("Hello World hello") == True, "Hello"
    assert three_words("He is 123 man") == False, "123 man"
    assert three_words("1 2 3 4") == False, "Digits"
    assert three_words("bla bla bla bla") == True, "Bla Bla"
    assert three_words("Hi") == False, "Hi"
