import googlemaps
from datetime import datetime
import pprint

KEY_GG = "AIzaSyAOHlya1GAyQTeBMrrAd_WOMe7VqCDUmNs"
pp = pprint.PrettyPrinter(indent=2)

class LocationDetector():
    def __init__(self):
        self.gmaps = googlemaps.Client(key=KEY_GG)

    def detect_location(self,loc):
        return self.get_coordinates(loc)

    def get_coordinates(self,loc):
        geocode_result = self.gmaps.geocode(loc)
        if geocode_result :
            location_lat = geocode_result[0]['geometry']['location']['lat']
            location_lng = geocode_result[0]['geometry']['location']['lng']
            return {"lat":location_lat,'lng':location_lng,"name":loc}
        return None
        # return loc

if __name__ == "__main__":
    locationDetector = LocationDetector()
    locationDetector.get_coordinates("quận thanh xuân hà nội ")