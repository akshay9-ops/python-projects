capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nest list in Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# Goal: Print Lille

#print(travel_log["France"][1])

#Nested list:
# nested_list = ["A", "B", ["C", "D"]]
#
# print(nested_list[2][0])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "num_times_visited": 8
    },
    "Germany": {
        "cities_visited":["Stuttgart", "Berlin"],
        "num_times_visited": 5
    }
}

print(travel_log["Germany"]["cities_visited"][0])