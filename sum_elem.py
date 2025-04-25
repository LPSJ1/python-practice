def sum_list():#First off I've initialized the function sum_list for adding numbers in allist

    numbers = input("Enter numbers(space each number):")
    # The user is prompted to input numbers and its stored in the variable called numbers
    numbers = [int(numie) for numie in numbers.split()]
    #the input from the user is converted from string to integer and split hence why you space the numbers
    #its temporarily stored in the variable called numie
    total = 0 #we're starting our count at 0
    for numie in numbers:
        total += numie
    #the for loop goes step by step in through the list from 'numbers' and adding each number to the total
    return total
#the function returns the sum

print("The sum is:", sum_list())
#the print stament calls the function and prints the result of the sum