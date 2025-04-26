def factorial():
    number = int(input("Enter numero(number): "))

    factorial = 1

    for n in range(1, number + 1):
        factorial *= n

    print(f"The factorial of {number} is {factorial}.")

factorial()    

#First, I got the user to insert a number and its stored in the variable number
#I started the factorial at 1 because is it was 0 the final answer would be 0
#the nnumber is used as n in the for loop and it multiplies the number folllowing the next one
#until the specified number is reached and finally the function is called in the end for execution