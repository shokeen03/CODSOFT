
import string
import random

L=[]

p1 = list(string.ascii_lowercase)
p2 = list(string.ascii_uppercase)
p3 = list(string.digits)
p4 = list(string.punctuation)

L.extend(p1)
L.extend(p2)
L.extend(p3)
L.extend(p4)

input_length = input("Enter length of your password: ")

while True:
 
    try:
 
        password_length = int(input_length)
 
        if password_length < 8:
 
            print("Your length should be 8 atleast.")
 
            input_length = input("Oops, Enter your length again: ")
 
        else:
 
            break
 
    except:
 
        print("Please, Enter numbers only to generate password.")
 
        input_length = input("Enter length of your password: ")


random.shuffle(L)

password = "".join(L[0:password_length])
print("Your Generated Password is: ", password)

