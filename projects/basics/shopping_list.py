#!/usr/local/bin/python3

from sys import exit


def help():
    print("""Enter 'end' to STOP this program and display the shopping list.
Enter 'show' to display the items in shopping list.
Enter 'count' to display the number of items in the shopping list.
Enter 'help' to display help message.""")


def display(items):
    if len(items) > 0:
        print("Here's the shopping list: ")
        for item in shopping_list:
            print(item)


def count(list_name):
    print("We have {} items in our shopping list.".format(len(list_name)))

if __name__ == "__main__":
    shopping_list = []
    print("What should we buy at the store?")
    print("Type 'help' for available options.")
    while True:
        try:
            new_item = input("> ")
        except KeyboardInterrupt:
            print("Quitting the program now.")
            exit(2)
        else:
            if new_item.lower() == "end":
                display(shopping_list)
                break
            elif new_item.lower() == "help":
                help()
                continue
            elif new_item.lower() == "show":
                display(shopping_list)
                continue
            elif new_item.lower() == "count":
                count(shopping_list)
                continue
            # The following commented lines are avoided with continue statement
            # after calling help, count and show. Comment continue statements
            # and check to see if the 'help' and 'show' gets into the list.
            # if not (new_item.lower() == "show" or
            #         new_item.lower() == "end" or
            #         new_item.lower() == "help"):
            shopping_list.append(new_item)
