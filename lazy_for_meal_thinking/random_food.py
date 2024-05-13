import googlemaps
from datetime import datetime
import pprint
import time
import random

google_map_api_key = 'insert your google map key'

def find_restaurants(location):
    gmaps = googlemaps.Client(key=google_map_api_key)
    
    p = gmaps.geocode(location)
    lat=str(p[0]['geometry']['location']['lat'])
    lng=str(p[0]['geometry']['location']['lng'])
    place = lat+ ', '+ lng
    places = gmaps.places_nearby(location=place,  max_price=3, open_now=True, radius=2000, type='food, restaurant')
    #pprint.pprint(places)
    restaurants = []
    for place in places['results']:
        restaurants.append(place['name'])
    for i, restaurant in enumerate(restaurants, 1):
        print("{}. {}".format(i, restaurant))
    
    return restaurants

def choose_random_restaurant(place):
    restaurants = find_restaurants(place)
    if restaurants:
        return random.choice(restaurants)
    else:
        return "Found nothong"


def main():
    place = input("Insert the country：")
    choose = choose_random_restaurant(place)
    
    
    for j in range(3):
	    print('Loading',end='')
	    for i in range(3):   
		    print('.',end='',flush=True)
		    time.sleep(1)   
	    print('\r'+' '*10+'\r',end='')

    print("\n###########################################\n\n"
          + "XD Let't eat here ->    "
          + choose +
          "\n\n###########################################\n")
if __name__ == "__main__":
    main()

