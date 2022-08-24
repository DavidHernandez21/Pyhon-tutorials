import jmespath

data = {
    'locations': [
        {'name': 'Seattle', 'state': 'WA'},
        {'name': 'New York', 'state': 'NY'},
        {'name': 'Bellevue', 'state': 'WA'},
        {'name': 'Olympia', 'state': 'WA'},
    ],
}

print(
    jmespath.search(
        "locations[?state == 'WA'].name | sort(@)[-2:] | {WashingtonCities: join(', ', @)}",
        data,
    ),
)
