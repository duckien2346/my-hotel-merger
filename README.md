# my-hotel-merger

[![License: MIT](https://img.shields.io/badge/License-GPLv3-yellow.svg)](https://opensource.org/licenses/GPL-3.0)

This is a merging hotels tool that merges hotels data from different sources into a single source.

There are 3 suppliers that will be fetched data from and their respective URLs (you can click on these links to check out their responses):

- https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme
- https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/patagonia
- https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies

This is a take-home assignment from Ascenda and here is [a detail requirement](https://gist.github.com/vu-hoang-kaligo/73a40b9db4fe079caf83bcb618177bd1)


## How to use it

It's recommended to use a virtualenv:

```bash
python3 -m venv venv
pip install my-hotel-merger
```

or

```bash
make venv
```


## Introduction

- A CLI application accepts 2 arguments for filtering: `hotel_ids` and `destination_ids` (ordering is important)
  - The format of both these arguments is a string that contains a list of value, each of which is separated by a comma `,`
  - In the case that the list is empty, the value of the argument is `none`.
  - Some examples:

```bash
my_hotel_merger hotel_id_1,hotel_id_2,hotel_id_3 destination_id_1,destination_id_2
my_hotel_merger hotel_id_4,hotel_id_5 none
my_hotel_merger none destination_id_3
```

- When called, the application should print an array of hotel data in JSON format to standard output. The structure of the hotel data is shown below.
  - The returned hotels should match all of the provided hotel_ids and destination_ids in the input. If a hotel matches the destination_ids but not hotel_ids, it shouldn't be returned.
  - If no hotel_id or destination_id is provided in the input, return all hotels.
- Each hotel should be returned only once (since you've already uniquely merged the data)


The JSON response from your implementation should match the following structure:

```json
[
  {
    "id": "iJhz",
    "destination_id": 5432,
    "name": "Beach Villas Singapore",
    "location": {
      "lat": 1.264751,
      "lng": 103.824006,
      "address": "8 Sentosa Gateway, Beach Villas, 098269",
      "city": "Singapore",
      "country": "Singapore"
    },
    "description": "Surrounded by tropical gardens, these upscale villas in elegant Colonial-style buildings are part of the Resorts World Sentosa complex and a 2-minute walk from the Waterfront train station.",
    "amenities": {
      "general": ["outdoor pool", "indoor pool", "business center", "childcare", "wifi", "dry cleaning", "breakfast"],
      "room": ["aircon", "tv", "coffee machine", "kettle", "hair dryer", "iron", "bathtub"]
    },
    "images": {
      "rooms": [
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/2.jpg", "description": "Double room" },
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/3.jpg", "description": "Double room" },
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/4.jpg", "description": "Bathroom" }
      ],
      "site": [
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/1.jpg", "description": "Front" }
      ],
      "amenities": [
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/0.jpg", "description": "RWS" }
      ]
    },
    "booking_conditions": [
      "All children are welcome. One child under 12 years stays free of charge when using existing beds. One child under 2 years stays free of charge in a child's cot/crib. One child under 4 years stays free of charge when using existing beds. One older child or adult is charged SGD 82.39 per person per night in an extra bed. The maximum number of children's cots/cribs in a room is 1. There is no capacity for extra beds in the room.",
      "Pets are not allowed.",
      "WiFi is available in all areas and is free of charge."
    ]
  }
]
```


## To run pylint:

Install python dependencies and run python linter
```
  make venv
  make pylint
```
