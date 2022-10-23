from datetime import datetime

def age_calc(year):
    today = datetime.today()    # instantiate the today object from the datetime module
    current_year = today.year   # using the .year to get the current year from the instantiation above
    age = current_year-year     # the difference between current year and your birth year results to your supposed age in that year
    return f"Your age = {age}yrs old"  # return the age

output = age_calc(1999) # assigning the function name with paramenters to a variable
print(output) # printing out the age in the console
