from operator import itemgetter

products = {"Headphones": 55.90, "USB drive": 12.20, "Ethernet Cable": 8.12, "Smartwatch": 125.80}

sort_by_price = sorted(products.items(), key=itemgetter(1))
print(sort_by_price)
# [('Ethernet Cable', 8.12), ('USB drive', 12.2), ('Headphones', 55.9), ('Smartwatch', 125.8)]

# Find index of maximum value in array
prices = [55.90, 12.20, 8.12, 99.80, 18.30]
index, price = max(enumerate(prices), key=itemgetter(1))
print(index, price)
# 3, 99.8

# Sort list of tuples based on their indices
names = [
    ("John", "Doe"),
    ("Andy", "Jones"),
    ("Joseph", "Smith"),
    ("Oliver", "Smith"),
]

print(sorted(names, key=itemgetter(1, 0)))