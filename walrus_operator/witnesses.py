cities = ["Vancouver", "Oslo", "Houston", "Warsaw", "Graz", "Holguín"]

# print(set(cities[1]) & set("z"))

# Does ANY city name start with "H"?
any(city.startswith("H") for city in cities)


# Does ANY city name have at least 10 characters?
any(len(city) >= 10 for city in cities)


# Do ALL city names contain "a" or "o"?
all(set(city) & set("ao") for city in cities)


# Do ALL city names start with "H"?
all(city.startswith("H") for city in cities)


if any((witness := city).startswith("H") for city in cities):
    print(f"{witness} starts with H")
else:
    print("No city name starts with H")


if all((witness := city).startswith("H") for city in cities):
    print("No city name starts with H")
else:
    print(f"{witness} does not start with H")