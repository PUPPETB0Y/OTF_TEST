# This module is to fix all the phone numbers in the property "phone" by adding the country code #
# The simplest way to do it since I found out all the information saved is from english countries is to make a dictionary with all the
#english countries as keys and their phones code as values #
#The argument required is a list of dictionaries that have the keys "country" and "phone", the return object is the same list but the phone value fixed #
import requests
# Retrieve country codes from the name of the country 
def get_country_code(country):
    # This are the countries I found are english speakers #
    phone_code = {"United Kingdom": "44","Australia":"43","Bahamas":"1-242","Barbados":"1-246","Belize":"501","Canada":"1","Dominica":"1-767","Grenada":"1-473","Guyana":"592","Ireland":"353",
     "Jamaica":"1-876","Malta":"356","New Zealand":"64","Saint Lucia":"1-758","United States":"1"}
    #This part of the code returns the phone code depending which country match with the argument #
    for option in phone_code:
        if country == option:
            return phone_code[option]
        
# This is the main function which adds the country code to each phone number
def fix_number(phone_list):
    for item in phone_list:
        country_name = item["country"] #Extracting the country name
        country_code = get_country_code(country_name)
        if country_code:
            phone_number= item["phone"] #Extracting the phone number
            phone_number=phone_number.replace("-","") #Here I try to follow the format which is  (+NNN) NNN NNNNNN by deleting the "-"
            if phone_number[0]=='0': #As said, in case the phone number starts with a 0 it must be completed after it
                item["phone"]=f"(+{country_code}) {phone_number[1:4]} {phone_number[4:]}"
            else:                                                                       #Here we add the spaces in the 4th indx and after the parenthesis
                item["phone"] = f"(+{country_code}) {phone_number[:4]} {phone_number[4:]}"
    return phone_list
