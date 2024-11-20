from my_hotel_merger.utils.helpers import Helper

class Location:
    """Location class for hotel"""
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
    """Amenities class for hotel"""
    general: list[str] | None
    room: list[str] | None
    def __init__(self, general=None, room=None):
        formatters = Helper.amenities_formatter()
        self.general = Helper.format_list_str(general, formatters)
        self.room = Helper.format_list_str(room, formatters)

class ImageItem:
    """Image item class for Images"""
    link: str | None
    description: str | None
    def __init__(self, link=None, description=None):
        self.link = Helper.format_str(link)
        self.description = Helper.format_str(description)

class Images:
    """Images class for hotel"""
    rooms: list[ImageItem] | None
    site: list[ImageItem] | None
    amenities: list[ImageItem] | None
    def __init__(self, rooms=None, site=None, amenities=None):
        self.rooms = rooms
        self.site = site
        self.amenities = amenities

class Hotel:
    """Hotel class"""
    id_: str
    destination_id: int
    name: str | None = None
    location: Location | None = None
    description: str | None = None
    amenities: Amenities | None = None
    images: Images | None = None
    booking_conditions: list[str] | None = None
    def __init__(self, id_: str, destination_id: int) -> None:
        self.id_ = id_
        self.destination_id = destination_id
