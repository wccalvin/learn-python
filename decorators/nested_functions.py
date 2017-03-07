#!/usr/local/bin/python3
def parent():

    print("This is parent()")

    def first_child():
        print("This will not be called...")
        return "This is first_child()"

    def second_child():
        return "This is second_child()"

    print(second_child())

if __name__ == "__main__":
    parent()
