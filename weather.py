import requests as req

#create a function that will search weather based on a zipcode
def weather(zip):
    print(f"Weather for {zip}:")
    resp = req.get(f"https://dataservice.accuweather.com/locations/v1/postalcodes/search?apikey=NZfVPriPMwZZN096wZTlt2wfYM7rC93N&q={zip}")
    print(resp.text)

#get user input for zip code
zip = input('Zip Code: ')

#call weather function to get weather for specified zip code
weather(zip)