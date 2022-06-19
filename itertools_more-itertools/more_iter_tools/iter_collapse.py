import more_itertools
# import os

# Get flat list of all files and directories
# print(list(os.walk('.')))
# print(list(more_itertools.collapse(list(os.walk(".")))))
# Get all nodes of tree into flat list
tree = [40, [25, [10, 3, 17], [32, 30, 38]], [78, 50, 93]]  # [Root, SUB_TREE_1, SUB_TREE_2, ..., SUB_TREE_n]
print(list(more_itertools.collapse(tree)))

iterable = ['ab', ('cd', 'ef'), ['gh', 'ij', ('kl', 'mn')]]
print(list(more_itertools.collapse(iterable, base_type=tuple)))

iterable = [('a', ['b']), ('c', ['d'])]
print(list(more_itertools.collapse(iterable, levels=1)))