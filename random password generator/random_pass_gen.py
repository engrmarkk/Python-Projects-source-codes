import string
import random


def password_gen():
    # To get the alphabets in lower case
    lower_case = string.ascii_lowercase

    # To get the alphabets in upper case
    upper_case = string.ascii_uppercase

    # To get the number 0 to 9
    digits = string.digits

    # To get all the symbols
    symbols = string.punctuation

    # To concatenate the lowercase alphabets, uppercase alphabets, digits and symbols
    big_string = lower_case+upper_case+digits+symbols

    # pick up 8 characters randomly from the concatenated value and return it as a list
    ran_pass = random.sample(big_string, 8)

    # Join all the values in the list to form a string
    password = ''.join(ran_pass)

    # print out the generated password
    print(password)


# invoking the function
password_gen()
