from helpers import Helper

class Location:
    lat: float | None
    lng: float | None
    address: str | None
    city: str | None
    country: str | None
    def __init__(self, lat=None, lng=None, address=None, city=None, country=None):
        self.lat = lat
        self.lng = lng
        self.address = Helper.format_str(address)
        self.city = Helper.format_str(city)
        self.country = Helper.format_str(country)

class Amenities:
    general: list[str] | None
    room: list[str] | None
    def __init__(self, general=None, room=None):
        formatters = Helper.amenities_formatter()
        self.general = Helper.format_list_str(general, formatters)
        self.room = Helper.format_list_str(room, formatters)

class ImageItem:
    link: str | None
    description: str | None
    def __init__(self, link=None, description=None):
        self.link = Helper.format_str(link)
        self.description = Helper.format_str(description)

class Images:
    rooms: list[ImageItem] | None
    site: list[ImageItem] | None
    amenities: list[ImageItem] | None
    def __init__(self, rooms=None, site=None, amenities=None):
        self.rooms = rooms
        self.site = site
        self.amenities = amenities

class Hotel:
    id: str
    destination_id: int
    name: str | None
    location: Location | None
    description: str | None
    amenities: Amenities | None
    images: Images | None
    booking_conditions: list[str] | None
    def __init__(self, id, destination_id, name=None, location=None, description=None, amenities=None, images=None, booking_conditions=None):
        self.id = id
        self.destination_id = destination_id
        self.name = Helper.format_str(name)
        self.location = location
        self.description = Helper.format_str(description)
        self.amenities = amenities
        self.images = images
        self.booking_conditions = Helper.format_list_str(booking_conditions)

