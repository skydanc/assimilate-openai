import random

fruits = ["apple", "banana", "orange", "pear", "grape", "strawberry", "watermelon"]
dishes = ["pizza", "burger", "pasta", "sushi", "salad", "soup", "steak"]

random_fruits = random.sample(fruits, 5)
random_dishes = random.sample(dishes, 5)

random_meals = []

for i in range(5):
    random_meals.append(random_fruits[i])
    random_meals.append(random_dishes[i])

print(random_meals)