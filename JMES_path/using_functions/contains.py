import jmespath

data = {
    'people': [
        {'age': 20, 'tags': ['a', 'b', 'c'], 'name': 'Bob'},
        {'age': 25, 'tags': ['d', 'e', 'f'], 'name': 'Fred'},
        {'age': 30, 'tags': ['g', 'e', 'i'], 'name': 'George'},
    ],
}
print(jmespath.search("people[?contains(tags, 'e')].{name: name}", data))
