#tuples and set (i have problem on this topic)

food_preferences = ("burger", "pizza", "pasta")

restaurants ={
    "seafood_cove":{"paste", "fish", "chips"},
    "hungry_jacks": {"burger", "fries", "pizza"},
    "potting_shed": {"carrot", "lettuce", "tomato"},


}

best_match_food = set()
best_match_restaurant = None

for restaurant_name, menu in restaurants.items():
    common_foods = food_preferences.intersection(menu)
    if len(common_foods) > len(best_match_food):
        best_match_food = common_foods
        best_match_restaurant = restaurant_name

print(f"The best match is {best_match_restaurant} with {(best_match_food)} matched foods.")
#result should be hungry_jacks with  burger and pizza