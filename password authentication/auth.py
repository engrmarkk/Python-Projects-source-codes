# defining a function passing the password parameter
def authenticate_password(password):
    # turning the password to a set
    letters = set(password)
    # checking if any of the letters from the set above is lowercase, uppercase and has a digit atleast 
    passed = (
        any(letter.islower() for letter in letters)
        and any(letter.isupper() for letter in letters)
        and any(letter.isdigit() for letter in letters)
    )
    
    # if the lenght of the password is less than 8 and 
    # any letter does not pass the requirement above, 
    # run this lines of code
    if not passed and len(password) < 8:
        # set auth to be false
        auth = False
        # while auth is false
        while not auth:
            # print this
            print(
                "\n- Password should have 8 character\n- Password should contain at least an uppercase, lowercase and a number\n"
            )
            # and prompt the user to enter the password again
            password = input(">> ")
            # turning the inputted password to a set once again
            letters = set(password)
            # check again if any of the letters from the set above is lowercase, uppercase and has a digit atleast 
            passed = (
                any(letter.islower() for letter in letters)
                and any(letter.isupper() for letter in letters)
                and any(letter.isdigit() for letter in letters)
            )
            # if all the requirements are passed
            if passed and len(password) > 7:
                # set auth to be true, and break out of the while loop
                auth = True

    # if all the requirements passed, print this
    print("\nRegistered Successfully\n")


# invoking the function
authenticate_password(input("Enter your password to get registered\n> "))
