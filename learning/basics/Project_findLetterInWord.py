def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

status = find("clayton", "c")

if status != -1:
    print "Found match."
else:
    print "No match found."
