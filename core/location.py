LOCATIONS = [
    ("Q1858", "Ha Noi", 21.0278, 105.8342),
    ("Q36175", "Thanh Hoa", 20.1291, 105.3131),
    ("Q25281", "Dat Lat", 11.9416, 108.4383),
    ("Q1854", "Ho Chi Minh City", 10.8231, 106.6297)
]


class Location:
    @staticmethod
    def search(location_name):
        matched = [location for location in LOCATIONS if location[1] == location_name]
        if len(matched) == 0:
            return None
        data = matched[0]
        keys = ["id", "name", "lat", "long"]
        location = dict(zip(keys, data))
        return location
