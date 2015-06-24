"""slice: The operator [n:m] returns the part of the string from the n-eth character to the m-eth character.
   i.e. including the n and excluding the m."""

x = "my string"

"""
    "my string"
     |||||||||
     012345678
"""
slice = x[3:6] # includes the s(3) but excludes the i(6)

print slice


print x[:] #prints the whole string.
