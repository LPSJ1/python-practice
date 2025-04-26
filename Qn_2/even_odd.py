def even_odd_checker():
    numero = int(input("Give me a numero(number): "))
    #that is a variable called numero storing an integer 
    if numero % 2 == 0:
        print(f"{numero} is an even number")
    else:
        print(f"{numero} is an odd number")

even_odd_checker()    
        #I used an if else using modulo where the input from the user
        #would be divided by 2 and if it's divisible els its odd
        #I used an f-string rather than 'manually adding the values'
        #its simpler and cleaner in my opinon