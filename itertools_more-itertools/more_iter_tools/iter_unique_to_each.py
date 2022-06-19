from more_itertools import unique_to_each

# Graph (adjacency list)
graph = {'A': {'B', 'E'}, 'B': {'A', 'C'}, 'C': {'B'}, 'D': {'E'}, 'E': {'A', 'D'}}

print(unique_to_each({'B', 'E'}, {'A', 'C'}, {'B'}, {'E'}, {'A', 'D'} , {'F'}))