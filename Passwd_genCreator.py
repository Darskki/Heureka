import random
import string

print("Hello, Welcome to Password creator!")

#lenght pw
length = int(input("\nEnter the length of password: "))

#define data + stringascii
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation


#combinate
all = lower + upper + num + symbols

#random
temp = random.sample(all, length)

#create pw
password = "".join(temp)

#new password
print(password)
