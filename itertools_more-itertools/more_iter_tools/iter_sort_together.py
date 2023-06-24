from more_itertools import sort_together

cols = (
    ('John', 'Ben', 'Andy', 'Mary'),
    ('1994-02-06', '1985-04-01', '1998-03-14', '1998-03-14'),
    ('2020-01-06', '2019-03-07', '2020-01-08', '2018-08-15'),
)

print(sort_together(cols, key_list=(1, 2)))
