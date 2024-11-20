import requests
from my_hotel_merger.models.hotel import Hotel, Location, Amenities, Images, ImageItem
from my_hotel_merger.utils.helpers import Helper

class BaseSupplier:
    """Base class for supplier data fetcher"""
    def endpoint(self) -> str:
        """URL to fetch supplier data"""
        return ''

    def parse(self, obj: dict) -> Hotel:
        """Parse supplier-provided data into Hotel object"""
        print(obj)
        return Hotel("", 0)

    def fetch(self):
        """Fetch data from supplier"""
        url = self.endpoint()
        resp = requests.get(url)
        return [self.parse(dto) for dto in resp.json()]

    def _parse_images(self, obj: dict, link_key: str, description_key: str) -> Images | None:
        if not Helper.is_exist(obj, "images"):
            return None
        rooms: list[ImageItem] | None = None
        site: list[ImageItem] | None = None
        amenities: list[ImageItem] | None = None
        if Helper.is_exist(obj["images"], "rooms"):
            rooms = self.__parse_image_items(obj["images"]["rooms"], link_key, description_key)
        if Helper.is_exist(obj["images"], "site"):
            site = self.__parse_image_items(obj["images"]["site"], link_key, description_key)
        if Helper.is_exist(obj["images"], "amenities"):
            amenities = self.__parse_image_items(obj["images"]["amenities"], link_key, description_key)
        images=Images(
            rooms=rooms,
            site=site,
            amenities=amenities,
        )
        return images

    def __parse_image_items(self, obj: dict, link_key: str, description_key: str) -> list[ImageItem] | None:
        return [ImageItem(link=item[link_key], description=item[description_key]) for item in obj if item]


class Acme(BaseSupplier):
    """Acme supplier data fetcher"""
    def endpoint(self) -> str:
        return 'https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme'

    def parse(self, obj: dict) -> Hotel:
        hotel = Hotel(
            id_ = obj["Id"],
            destination_id = obj["DestinationId"],
        )
        hotel.name = Helper.format_str(obj["Name"])
        hotel.location = Location(
            lat=obj["Latitude"],
            lng=obj["Longitude"],
            address=obj["Address"],
            city=obj["City"],
            country=obj["Country"],
        )
        hotel.description = Helper.format_str(obj["Description"])
        hotel.amenities = Amenities(
            general=obj["Facilities"],
        )
        return hotel


class Patagonia(BaseSupplier):
    """Patagonia supplier data fetcher"""
    def endpoint(self) -> str:
        return 'https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/patagonia'

    def parse(self, obj: dict) -> Hotel:
        hotel = Hotel(
            id_ = obj["id"],
            destination_id = obj["destination"],
        )
        hotel.name = Helper.format_str(obj["name"])
        hotel.location = Location(
            lat=obj["lat"],
            lng=obj["lng"],
            address=obj["address"],
        )
        hotel.description = Helper.format_str(obj["info"])
        hotel.amenities = Amenities(
            room=obj["amenities"],
        )
        hotel.images = self._parse_images(obj, "url", "description")
        return hotel


class Paperflies(BaseSupplier):
    """Paperflies supplier data fetcher"""
    def endpoint(self) -> str:
        return 'https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies'

    def parse(self, obj: dict) -> Hotel:
        hotel = Hotel(
            id_ = obj["hotel_id"],
            destination_id = obj["destination_id"],
        )
        hotel.name = Helper.format_str(obj['hotel_name'])
        hotel.location = self.__parse_location(obj)
        hotel.description = Helper.format_str(obj["details"])
        hotel.amenities = self.__parse_amenities(obj)
        hotel.images = self._parse_images(obj, "link", "caption")
        hotel.booking_conditions = Helper.format_list_str(obj["booking_conditions"])
        return hotel

    def __parse_amenities(self, obj: dict) -> Amenities | None:
        if not Helper.is_exist(obj, "amenities"):
            return None
        return Amenities(
            general=obj["amenities"]["general"],
            room=obj["amenities"]["room"],
        )

    def __parse_location(self, obj: dict) -> Location | None:
        if not Helper.is_exist(obj, "location"):
            return None
        return Location(
            address=obj["location"]["address"],
            country=obj["location"]["country"],
        )
