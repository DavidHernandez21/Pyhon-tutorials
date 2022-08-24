import jmespath

data = {
    'people': [
        {'age': 20, 'tags': ['a', 'b', 'c'], 'name': 'Bob'},
        {'age': 25, 'tags': ['d', 'e', 'f'], 'name': 'Fred'},
        {'age': 30, 'tags': ['g', 'h', 'i'], 'name': 'George'},
    ],
}

# print(jmespath.search("people[?age<=`25`]", data))
# list
print(
    jmespath.search('people[?age > `20`].[name, age]', data),
)  # [["George", 30], ["Fred", 25]]

# hash (dict)
print(
    jmespath.search('people[?age > `20`].{name: name, age: age}', data),
)  # [{'name': 'Fred', 'age': 25}, {'name': 'George', 'age': 30}]
print(
    jmespath.search('people[?age > `20`].{name: name, tags: tags[0]}', data),
)  # [{'name': 'Fred', 'tags': 'd'}, {'name': 'George', 'tags': 'g'}]
