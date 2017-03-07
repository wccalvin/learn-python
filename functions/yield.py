#!/usr/local/bin/python3


def square(num):
    for i in range(num):
        yield i**2

if __name__ == "__main__":
    gen_obj = square(10)
    print(gen_obj)
    data = [i for i in gen_obj]
    print(data)
