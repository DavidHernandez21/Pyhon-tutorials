from itertools import groupby
from operator import itemgetter

rows = [
    {'name': 'John', 'surname': 'Doe', 'id': 2},
    {'name': 'Andy', 'surname': 'Smith', 'id': 1},
    {'name': 'Joseph', 'surname': 'Jones', 'id': 3},
    {'name': 'Oliver', 'surname': 'Smith', 'id': 4},
]


sorted_by_name = sorted(rows, key=itemgetter('surname', 'name'))
# print(sorted_by_name)


# print(min(rows, key=itemgetter("id")))


orders = [
    {'date': '07/10/2021', 'id': 10001},
    {'date': '07/10/2021', 'id': 10002},
    {'date': '07/12/2021', 'id': 10003},
    {'date': '07/15/2021', 'id': 10004},
    {'date': '07/15/2021', 'id': 10005},
]


orders.sort(key=itemgetter('date'))
for date, rows in groupby(orders, key=itemgetter('date')):
    print(f'On {date}:')
    for order in rows:
        print(order)
    print()
