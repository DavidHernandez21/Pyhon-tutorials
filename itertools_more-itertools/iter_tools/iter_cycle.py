from itertools import cycle
from itertools import islice

players = ("John", "Ben", "Martin", "Peter", "David")

next_player = cycle(players).__next__
player = next_player()
print(player)
#  "John"

player = next_player()
print(player)
#  "Ben"
#  ...

# Infinite Spinner
# import time

# for c in cycle('/-\|'):
#     print(c, end = '\r')
#     time.sleep(0.2)

print(list(islice(cycle(players), 2, 4)))
