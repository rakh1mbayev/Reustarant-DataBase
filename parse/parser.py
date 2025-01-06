import requests
import random
import json

# API
API_KEY = "wDS2Cysxg7LSxkhqkN065zvNvXkklzm9G0bAesxqcx7jfpAuJlDuXmRTXNnMP_a7M4ydteuVMnuOFRiZ3ssO14YI38tifjvuB8jgyO6Lm1P16qQw5TVwnIoVY916Z3Yx"
headers = {"Authorization": f"Bearer {API_KEY}"}
search_url = "https://api.yelp.com/v3/businesses/search"
details_url = "https://api.yelp.com/v3/businesses/"

categories = ["Appetizer", "Main Course", "Dessert", "Beverage", "Salad", "Soup"]

dishes = [
    "Spaghetti Carbonara", "Grilled Chicken", "Cheeseburger", "Caesar Salad", "Tom Yum Soup",
    "Margherita Pizza", "Peking Duck", "Fish Tacos", "Lasagna", "Tiramisu",
    "Vegetable Stir Fry", "Chicken Parmesan", "Mushroom Risotto", "Beef Wellington",
    "Fried Calamari", "Lamb Chops", "Shrimp Scampi", "Fettuccine Alfredo", "Chocolate Cake",
    "Apple Pie", "Green Curry", "Roast Beef", "Pad Thai", "Seafood Paella"
]

prices = [5.99, 10.99, 12.99, 15.99, 18.99, 7.99, 14.99, 9.99, 20.99, 6.99]

# Random menu
def generate_random_menu(num_dishes=5):
    menu = []
    for i in range(num_dishes):
        dish = random.choice(dishes)
        category = random.choice(categories)
        price = random.choice(prices)
        menu.append({
            "_id": str(i + 1),
            "name": dish,
            "category": category,
            "price": round(price, 2)
        })
    return menu

# Parameters for request
params = {
    "term": "restaurant",
    "location": "New York",
    "limit": 50  # 50 restaurants for query
}

all_restaurants = []

# 20 queries with 50 restaurants
for offset in range(0, 1000, 50):
    params["offset"] = offset
    response = requests.get(search_url, headers=headers, params=params)
    data = response.json()

    # Current restaurants
    for i, business in enumerate(data.get("businesses", [])):
       
        business_id = business.get("id")
        
        # Information about restaurant
        details_response = requests.get(details_url + business_id, headers=headers)
        details_data = details_response.json()

        # Forming structure
        restaurant = {
            "_id": str(offset + i + 1),  # Уникальный ID для каждого ресторана
            "name": business.get("name"),
            "location": ", ".join(business["location"].get("display_address", [])),
            "cuisine": ", ".join([cat["title"] for cat in business.get("categories", [])]),
            "contact": business.get("phone"),
            "dishes": []  # Пустое меню по умолчанию
        }
        
        # Adding random menu
        restaurant["dishes"] = generate_random_menu(num_dishes=7)

        all_restaurants.append(restaurant)

# Final JSON
result = {"restaurants": all_restaurants}

# Saving in JSON
with open("yelp_restaurants_1000_with_menu.json", "w") as file:
    json.dump(result, file, indent=4)

print("JSON сохранен в файл yelp_restaurants_1000_with_menu.json")
