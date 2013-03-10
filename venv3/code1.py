import googlemaps

def printlatlong(api_key, address):
    # address should be something like '1312 Massachusetts Avenue, Cambridge MA'
    
    maps = GoogleMaps(api_key)
    lat, lng = maps.address_to_latlng(address)
    return (lat, lng)

printlatlong(AIzaSyBx7Z2Z6n7m1XPi8prdhgNIa0P7EmOX38I, '1312 Mass Ave. Cambridge MA')
