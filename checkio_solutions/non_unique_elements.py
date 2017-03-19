#!/usr/local/bin/python3


def non_unique(data):
    non_unique = []
    for elem in data:
        if data.count(elem) > 1:
            non_unique.append(elem)
    return non_unique

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert isinstance(non_unique([1]), list), "The result must be a list"
    assert non_unique([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert non_unique([1, 2, 3, 4, 5]) == [], "2nd example"
    assert non_unique([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert non_unique([10, 9, 10, 10, 9, 8]) == [
        10, 9, 10, 10, 9], "4th example"
