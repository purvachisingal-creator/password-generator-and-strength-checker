import random
import string
import re
def generate_password(length):
    # string.ascii_lowercase
    # string.ascii_lowercase
    # string.digits
    # string.punctuation
    pool = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase
    password = ""
    for i in range(length):
        password += random.choice(pool)
    return password

def strength_check(password):
    safe_punctuation = re.escape(string.punctuation)
    li = "[" + safe_punctuation + "]"
    point = 0
    if re.search("[a-z]", password):
        point += 1
    if re.search("[A-Z]", password):
        point += 1
    if re.search("[0-9]", password):
        point += 1
    if re.search(li, password):
        point += 1

    if point == 0:
        return ("not valid password")
    elif point == 1:
        return ("weak password")
    elif point == 2 or point == 3:
        return ("medium password")
    elif point == 4:
        return ("strong password")
    else:
        return ("not valid password")
def main():
    length = int(input("Enter the length of the password: "))
    while True:
        password = generate_password(length)
        strength = strength_check(password)
        print(password,"-",strength)
        if strength == "strong password":

            break
        print("attempt failed..trying again")

if __name__ == "__main__":
    main()