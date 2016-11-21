def checkio(number):
    number_list = [i for i in list(str(number)) if not i == '0']
    product = 1
    for i in range(0, len(number_list)):
        product *= int(number_list[i])
    return product


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
