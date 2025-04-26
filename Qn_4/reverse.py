def reverse_string():
    word = input("gimme a word user!:")

    reversed_list = []

    for char in word:

        reversed_list.insert(0, char)

    return "".join(reversed_list)    

print(f"the word is {reverse_string()}")
  

#This function picks a word from the user and stores it in the variable called word
#an empty list is created called reversed_list
#the for loop goes through the word and inserts each character at the beginning of the list
#the list is then joined together and returned as a string
#the print statement calls the function and prints the result of the reversed word
#I think this is a good way to reverse a string because it uses a list and the insert method which I got off a youtube video