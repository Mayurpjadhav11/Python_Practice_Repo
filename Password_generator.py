import random
import string

upper_case = list(string.ascii_uppercase)
lower_case = list(string.ascii_lowercase)
digits = list(string.digits)
special_characters = list(string.punctuation)

upper_case_length = int(input("Enter the number of uppercase letters you want in your password: "))
lower_case_length = int(input("Enter the number of lowercase letters you want in your password: "))
digits_length = int(input("Enter the number of digits you want in your password: "))
special_characters_length = int(input("Enter the number of special characters you want in your password: "))

password = []
for i in range(0, upper_case_length):
    password.append(random.choice(upper_case))
for i in range(0, lower_case_length):
    password.append(random.choice(lower_case))
for i in range(0, digits_length):
    password.append(random.choice(digits))
for i in range(0, special_characters_length):
    password.append(random.choice(special_characters))


random.shuffle(password)
password="".join(password)
print(password)