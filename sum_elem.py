def sum_list():#First off I've initialized the function sum_list for adding numbers in allist

    numbers = input("Enter numbers(space each number):")
    # The user is prompted to input numbers and its stored in the variable called numbers
    numbers = [int(numie) for numie in numbers.split()]
    #the input from the user is converted from string to integer and split hence why you space the numbers
    total = 0

    for numie in numbers:
        total += numie

    return total

print("The sum is:", sum_list())