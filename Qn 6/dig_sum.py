def digisum():

    number = input("Enter a number:")

    total = 0

    for digit in number:
        total += int(digit)

    print(f"The sum of the digits in {number} is {total}.")

digisum()        
#The user enters thr number stored in variable number
#the total is srt to 0 then the for loop picks each digit in the number and adds
# it to the total 
#finally the print statement prints the result of the sum