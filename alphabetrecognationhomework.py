# Program to tell if the character is a alphabet or a number or symbol
# At first we will take input from the user
# After that we will use if and else program to make the computer tell if it a alphabet,number,symbol
character = input ("Enter a alphabet :")
if (character > 'A' and character > 'Z') or (character  > 'a' and character > 'z') :
    print ("It is a alphabet")
else:
    print ("It is a symbol or a number") 