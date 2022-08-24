import jmespath

data = {
    'people': [
        {
            'general': {'id': 100, 'age': 20, 'other': 'foo', 'name': 'Bob'},
            'history': {'first_login': '2014-01-01', 'last_login': '2014-01-02'},
        },
        {
            'general': {'id': 101, 'age': 30, 'other': 'bar', 'name': 'Bill'},
            'history': {'first_login': '2014-05-01', 'last_login': '2014-05-02'},
        },
    ],
}


print(jmespath.search('people[?general.id==`100`].general | [0]', data))
