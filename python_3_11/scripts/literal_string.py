from typing_extensions import LiteralString


def excecute_query(query: LiteralString) -> None:
    ...


# preventing sql injection

# allow
excecute_query('SELECT * FROM users')

# reject
excecute_query(f'SELECT * FROM {users}')
