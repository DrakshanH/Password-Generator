import random
import string
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

# print(f"uppercase:- {uppercase}\nlowercase:- {lowercase}\ndigits:- {digits}\nsymbols:- {symbols}")

print("welcome to password generator!!")
print("---------------------------------")
upper = bool(input("do you want to use upper case letters? (1/0) "))
lower = bool(input("do you want to use lower case letters? (1/0) "))
num = bool(input("do you want to use digits? (1/0) "))
sym = bool(input("do you want to use symbols? (1/0) "))

all = ""

if upper:
    all+=uppercase
if lower:
    all+=lowercase
if num:
    all+=digits
if sym:
    all+=symbols


length = int(input("enter the length u want for ur password: "))
amount = 5 #you can change the amt obv

for x in range(amount):
    password = "".join(random.sample(all,length))
    print(password)
