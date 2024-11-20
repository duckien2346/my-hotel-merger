from typing import Callable
from models import Hotel, Location, Amenities, Images
from helpers import Helper

class HotelsService:
    def __init__(self):
        self.data: dict[str,Hotel] = {}
        self.raw_data: list[Hotel] = []

    def merge_and_save(self, raw_data: list[Hotel]):
        self.raw_data = raw_data
        for hotel in raw_data:
            key = f"{hotel.id}-{hotel.destination_id}"
            if not key in self.data:
                self.data[key] = hotel
            else:
                base = self.data[key]
                HotelsService.__merge_hotel(base, hotel)

    def find(self, hotel_ids, destination_ids) -> list[Hotel]:
        # Write your code here
        result: list[Hotel] = []
        for key, value in self.data.items():
            result.append(value)
        return result
        # return self.raw_data

    @staticmethod
    def __merge_hotel(base: Hotel, source: Hotel):
        base.name = HotelsService.__merge_name(base.name, source.name)
        base.location = HotelsService.__merge_location(base.location, source.location)
        base.description = HotelsService.__merge_description(base.description, source.description)
        base.amenities = HotelsService.__merge_amenities(base.amenities, source.amenities)
        base.images = HotelsService.__merge_images(base.images, source.images)
        base.booking_conditions = HotelsService.__merge_booking_conditions(base.booking_conditions, source.booking_conditions)

    @staticmethod
    def __merge_name(base: str | None, source: str | None) -> str | None:
        return HotelsService.__merge_str(base, source)

    @staticmethod
    def __merge_location(base: Location | None, source: Location | None) -> Location | None:
        if base is None or source is None:
            return base if source is None else source
        base.lat = HotelsService.__merge_float(base.lat, source.lat)
        base.lng = HotelsService.__merge_float(base.lng, source.lng)
        base.address = HotelsService.__merge_str(base.address, source.address)
        base.city = HotelsService.__merge_str(base.city, source.city)
        base.country = HotelsService.__merge_str(base.country, source.country)
        return base

    @staticmethod
    def __merge_description(base: str | None, source: str | None) -> str | None:
        return HotelsService.__merge_str(base, source)

    @staticmethod
    def __merge_amenities(base: Amenities | None, source: Amenities | None) -> Amenities | None:
        if base is None or source is None:
            return base if source is None else source
        return base

    @staticmethod
    def __merge_images(base: Images | None, source: Images | None) -> Images | None:
        if base is None or source is None:
            return base if source is None else source
        return base

    @staticmethod
    def __merge_booking_conditions(base: list[str] | None, source: list[str] | None) -> list[str] | None:
        if base is None or source is None:
            return base if source is None else source
        return base

    @staticmethod
    def __merge_list_str(base: list[str] | None, source: list[str] | None) -> list[str] | None:
        if base is None or source is None:
            return base if source is None else source
        for i in range(len(base)):
          # "general":["pool", "businesscenter", "wifi", "drycleaning", "breakfast"],
          # "general":["outdoor pool","indoor pool","business center","childcare"]
          # "general": ["outdoor pool", "indoor pool", "business center", "childcare", "wifi", "dry cleaning", "breakfast"],
            pass
        return base

    @staticmethod
    def __merge_str(base: str | None, source: str | None) -> str | None:
        if base is None or source is None:
            return base if source is None else source
        # assume that getting the longest string comes with the most information
        if Helper.compare_str(base, source) < 0:
            return source
        return base

    @staticmethod
    def __merge_float(base: float | None, source: float | None) -> float | None:
        # assume that if both are not None, they must be the same
        return base if source is None else source

