#print(evens_and_oddds(100))
#The number of odds are 50
#The number of evens are 51

def evens_and_odds(n):
    count_even = 0
    count_odd = 0
    for i in range(0, n + 1):
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    print(f"The number of odds are {count_odd}.")
    print(f"The number of evens are {count_even}.")

evens_and_odds(100)

#A function which returns an array of seven random numbers in a range of 0-9

import random

def shuffle_list(list):
    random.shuffle(list)
    return list

def random_unique_numbers():
    numbers = list(range(10))
    random_numbers = shuffle_list(numbers)[:7]
    return random_numbers

print(random_unique_numbers())


#Difference between a type error and value error

#TypeError: This error occurs when you try to perform an operation on a value of the wrong type. For example, trying to add a string and an integer together, or trying to call a function on a value that is not a function.
#ValueError: This error occurs when you try to perform an operation on a value that is of the correct type, but is not a valid value for that operation. For example, trying to convert a string that does not represent a valid integer to an integer, or trying to find the square root of a negative number.

