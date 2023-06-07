""" This module is to recognize if the value of the "Country" property is a city or a country.
This use the library "request" to access to the geoname api which helps to know the country of a city input, this api works with an user in the geoname's page.
The argument required is the city or country you want to search and the username, in case that the input is a city the return object is a tuple "(country,city)" if the input is a country it returns an empty city, 
if there is no searching results return "None", if there is an error returns the error. 
The algorithm returns the first country that match with the city name, for a better performance it will need also the coordinates of the location in case two or more names of cities are the same. 
As a default setting I let my username, but for better use and follow up submite your own account. 
The country is selected by extracting the first 3 countries that match with the city search and then it returns the one with more population  """


def get_city_info(city_name, username='david.pelaez'):
    import requests
    base_url = "http://api.geonames.org/searchJSON"

    #Construct the request payload
    params = {
        # You can find the meaning of this params in the follow link http://www.geonames.org/export/geonames-search.html #
        "q": city_name,
        "maxRows": 3,
        "username": username
    }

    #Collecting the info
    try:
        max_popultn=0
        response = requests.get(base_url, params=params)
        data = response.json()
    
        #Here we make sure there is info in the dictionary of geonames and return the answer
        if 'geonames' in data and len(data['geonames']) > 0:
            for i in range(len(data['geonames'])):
                try:
                    if (data['geonames'][i]['population']) > max_popultn:
                        max_popultn=data['geonames'][i]['population']
                        Country=data['geonames'][i]['countryName']
                        City_search=data['geonames'][i]['name']
                except:
                    print("There is a location that dom't have a country related")

            #Here we compare the city name of the input and the country name, if both match it means you serach the country and it returns an empty list, other case it returns the "(Country,City)"
            if (Country) != (City_search):
                return (Country, City_search )
            else:
                return (Country,"")
        else:
            return 'None'
    except requests.exceptions.RequestException as err:
        print("Error: ", err)
        return err
