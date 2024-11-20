from my_hotel_merger.models.hotel import Hotel, ImageItem, Location, Amenities, Images
from my_hotel_merger.utils.helpers import Helper

class HotelsService:
    """A HotelsService to merge and filter hotel data"""
    def __init__(self):
        self.data: dict[str,Hotel] = {}

    def merge_and_save(self, raw_data: list[Hotel]):
        """Merge the data and save it in-memory"""
        for hotel in raw_data:
            key = f"{hotel.id_}-{hotel.destination_id}"
            if key not in self.data:
                self.data[key] = hotel
            else:
                base = self.data[key]
                HotelsService.__merge_hotel(base, hotel)

    def find(self, hotel_ids: str, destination_ids: str) -> list[Hotel]:
        """Find and return the filtered data"""
        # If both are none, return all data
        if hotel_ids == 'none' and destination_ids == 'none':
            return list(self.data.values())

        # If one of them is none, return data based on the other
        if hotel_ids == 'none' or destination_ids == 'none':
            ids = hotel_ids if destination_ids == 'none' else destination_ids
            list_ids = ids.split(',')
            result: list[Hotel] = []
            for k, v in self.data.items():
                for id_ in list_ids:
                    if id_ in k:
                        result.append(v)
            return result

        # If both are not none, return data based on both
        list_hotel_ids = hotel_ids.split(',')
        list_destination_ids = destination_ids.split(',')
        result: list[Hotel] = []
        for hotel_id in list_hotel_ids:
            for destination_id in list_destination_ids:
                key = f"{hotel_id}-{destination_id}"
                if key in self.data:
                    result.append(self.data[key])
        return result

    @staticmethod
    def __merge_hotel(base: Hotel, source: Hotel):
        base.name = HotelsService.__merge_name(base.name, source.name)
        base.location = HotelsService.__merge_location(base.location, source.location)
        base.description = HotelsService.__merge_description(base.description, source.description)
        base.amenities = HotelsService.__merge_amenities(base.amenities, source.amenities)
        base.images = HotelsService.__merge_images(base.images, source.images)
        base.booking_conditions = HotelsService.__merge_bookin_condi(base.booking_conditions, source.booking_conditions)

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
        base.general = HotelsService.__merge_amenities_list_str(base.general, source.general)
        base.room = HotelsService.__merge_amenities_list_str(base.room, source.room)
        return base

    @staticmethod
    def __merge_images(base: Images | None, source: Images | None) -> Images | None:
        if base is None or source is None:
            return base if source is None else source
        base.rooms = HotelsService.__merge_images_list_item(base.rooms, source.rooms)
        base.site = HotelsService.__merge_images_list_item(base.site, source.site)
        base.amenities = HotelsService.__merge_images_list_item(base.amenities, source.amenities)
        return base

    @staticmethod
    def __merge_bookin_condi(base: list[str] | None, source: list[str] | None) -> list[str] | None:
        if base is None or source is None:
            return base if source is None else source
        return base

    # Helper methods

    @staticmethod
    def __merge_amenities_list_str(base: list[str] | None, source: list[str] | None) -> list[str] | None:
        if base is None or source is None:
            return base if source is None else source
        combined_list = base + source

        # Step 2: Remove duplicates by converting the list into a set
        combined_list = list(set(combined_list))

        # Step 3: Remove words that are substrings of other words
        filtered_list = []
        for word in combined_list:
            if not any(word != other_word and word in other_word for other_word in combined_list):
                filtered_list.append(word)

        return filtered_list

    @staticmethod
    def __merge_images_list_item(
            base: list[ImageItem] | None,
            source: list[ImageItem] | None) -> list[ImageItem] | None:

        if base is None or source is None:
            return base if source is None else source

        dict_base: dict[str,ImageItem] = {item.link: item for item in base if item.link}
        for item in source:
            if item.link is None:
                continue

            if item.link not in dict_base.keys():
                dict_base[item.link] = item
                continue

            dict_item = dict_base[item.link]
            if item.description is None or dict_item.description is None:
                continue
            compare = Helper.compare_str(dict_item.description, item.description)
            if compare < 0:
                # Assume that getting the longest string comes with the most information
                dict_item.description = item.description

        return list(dict_base.values())

    @staticmethod
    def __merge_str(base: str | None, source: str | None) -> str | None:
        if base is None or source is None:
            return base if source is None else source
        if Helper.compare_str(base, source) < 0:
            # Assume that getting the longest string comes with the most information
            return source
        return base

    @staticmethod
    def __merge_float(base: float | None, source: float | None) -> float | None:
        # assume that if both are not None, they must be the same
        return base if source is None else source
