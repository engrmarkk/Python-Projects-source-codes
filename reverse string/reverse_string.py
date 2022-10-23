"""
Using the slicing method to reverse a string in python, the index of a character in a string is 
lenght of the string -1, the :: indicates all character in the string while the -1 in the end, reverses the order
of the characters in the string  
"""
def str_rev(random_string):
    return random_string[::-1]

output = str_rev('python')
print(output)
