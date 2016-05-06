#!/usr/bin/env python
def hash(num):
    s = ""
    refer = "acdegilmnoprstuw"
    for i in range(0, 9):
        if num > 37:
            k = num % 37
            s = refer[k] + s
            num = num / 37
        else:
            return s
    return s

if __name__ == '__main__':
    num = long(raw_input("Enter the Number:"))
    result = hash(num)
    print result
