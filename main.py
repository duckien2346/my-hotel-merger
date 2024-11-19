import argparse
import json
from suppliers import Acme, Patagonia, Paperflies
from hotels_service import HotelsService

def fetch_hotels(hotel_ids, destination_ids):
    # Write your code here

    suppliers = [
        Acme(),
        Patagonia(),
        Paperflies(),
    ]

    # Fetch data from all suppliers
    all_supplier_data = []
    for supp in suppliers:
        all_supplier_data.extend(supp.fetch())

    # Merge all the data and save it in-memory somewhere
    svc = HotelsService()
    svc.merge_and_save(all_supplier_data)

    # Fetch filtered data
    filtered = svc.find(hotel_ids, destination_ids)

    # Return as json
    return json.dumps(filtered, default=lambda o: o.__dict__)
    
def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("hotel_ids", type=str, help="Hotel IDs")
    parser.add_argument("destination_ids", type=str, help="Destination IDs")

    # Parse the arguments
    args = parser.parse_args()

    hotel_ids = args.hotel_ids
    destination_ids = args.destination_ids

    result = fetch_hotels(hotel_ids, destination_ids)
    print(result)

if __name__ == "__main__":
    main()
