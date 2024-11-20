import requests
from models import *
from helpers import Helper

class BaseSupplier:
    def endpoint(self) -> str:
        """URL to fetch supplier data"""
        return ''

    def parse(self, obj: dict) -> Hotel:
        """Parse supplier-provided data into Hotel object"""
        return Hotel("id","des_id")

    def fetch(self):
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
    def endpoint(self) -> str:
        return 'https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme'

    def parse(self, obj: dict) -> Hotel:
        return Hotel(
            id=obj["Id"],
            destination_id=obj["DestinationId"],
            name=obj["Name"],
            location=Location(
                lat=obj["Latitude"],
                lng=obj["Longitude"],
                address=obj["Address"],
                city=obj["City"],
                country=obj["Country"],
            ),
            description=obj["Description"],
            amenities=Amenities(
                general=obj["Facilities"],
            ),
        )


class Patagonia(BaseSupplier):
    def endpoint(self) -> str:
        return 'https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/patagonia'

    def parse(self, obj: dict) -> Hotel:
        return Hotel(
            id=obj['id'],
            destination_id=obj['destination'],
            name=obj["name"],
            location=Location(
                lat=obj["lat"],
                lng=obj["lng"],
                address=obj["address"],
            ),
            description=obj["info"],
            amenities=Amenities(
                room=obj["amenities"],
            ),
            images=self._parse_images(obj, "url", "description"),
        )


class Paperflies(BaseSupplier):
    def endpoint(self) -> str:
        return 'https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies'

    def parse(self, obj: dict) -> Hotel:
        return Hotel(
            id=obj['hotel_id'],
            destination_id=obj['destination_id'],
            name=obj['hotel_name'],
            location=self.__parse_location(obj),
            description=obj["details"],
            amenities=self.__parse_amenities(obj),
            images=self._parse_images(obj, "link", "caption"),
            booking_conditions=obj["booking_conditions"],
        )

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

