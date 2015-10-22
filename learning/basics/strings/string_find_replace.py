__author__ = 'wccalvin'

# String search method
s = "This is fun"
find = s.find('f')
print("Index of the first occurence: {}".format(find)) # finds the index of the search string

# String replace method
print("Before replacing: {}".format(s))
replace = s.replace('fun', 'cool!')
print("After replacing: {}".format(replace))
