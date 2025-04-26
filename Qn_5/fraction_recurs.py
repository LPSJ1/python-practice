def factorial_recursion():

    number =int(input("Enter number:"))


    def calculate_factorial(x):

        if x == 0 or x == 1:

            return 1
        else:

            return  x * calculate_factorial(x-1)
        
    result = calculate_factorial(number)

    print(f"the factorial or {number} is {result}")

factorial_recursion()
# I got the user to insert a number and its stored in the variable number
# I created a function called calculate_factorial which takes in the number and checks if its 0 or 1
# if it is it returns 1 and if not it returns the number multiplied by the function itself with the number -1
# normally recursive functions call themselves until the base case is reached