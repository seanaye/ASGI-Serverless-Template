from ariadne import QueryType

QUERY = QueryType()


@QUERY.field('echo')
def r_echo(*_, name: str) -> str:
    return f'Hello: {name}'
