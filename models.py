
class Location:
    lat: float | None
    lng: float | None
    address: str | None
    city: str | None
    country: str | None

class Amenities:
    general: list[str] | None
    room: list[str] | None

class ImageItem:
    link: str | None
    description: str | None

class Images:
    rooms: list[ImageItem] | None
    site: list[ImageItem] | None
    amenities: list[ImageItem] | None

class Hotel:
    id: str
    destination_id: int
    name: str | None
    location: Location | None
    description: str | None
    amenities: Amenities | None
    images: Images | None
    booking_conditions: list[str] | None

