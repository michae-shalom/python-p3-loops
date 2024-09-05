#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    num=10
    while num>0:
        print(num)
        num -=1
    print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    return [x**2 for x in int_list]
    print (square_integers([1,2,3,4,5,6,7,8,9]))
    pass

def fizzbuzz():
    # code goes here!
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
    pass
