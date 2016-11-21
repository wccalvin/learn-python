def find_message(text):
    """Find a secret message"""
    text_list = list(text)
    all_caps = [i for i in text_list if i.isupper()]
    return "".join(all_caps)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"