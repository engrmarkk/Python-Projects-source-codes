from countryinfo import CountryInfo     #you have to pip install countryinfo

def country_info(my_country):
    country = CountryInfo(my_country)   # instantiate the imported CountryInfo from the module installed

    print(country.provinces())          # prints out the provinces of the states
    print(country.alt_spellings())      # prints out the alternatives spellings of the country
    print(country.area())               # prints out the number of square kilometer area of the country
    print(country.borders())            # prints out the bordering countries
    print(country.calling_codes())      # prints out the country's international calling codes
    print(country.capital())            # prints out the country's capital city
    print(country.capital_latlng())     # prints out the capital city latitude and longitude for the country's capital
    print(country.currencies())         # prints out the country's currency(ies)
    print(country.demonym())            # prints out the 
    print(country.languages())          # prints out the official language of the country
    print(country.native_name())        # prints out the name of the country in its native language
    print(country.population())         # prints out the approximate population of the country
    print(country.timezones())          # prints out the timezone(s) of the country
    print(country.region())             # prints out the country's continent

country_info("Nigeria")                 # Invoke the function
