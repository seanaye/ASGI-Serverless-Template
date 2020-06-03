from mangum import Mangum
from ariadne.asgi import GraphQL
from app.resolvers.schema import SCHEMA


handler = Mangum(GraphQL(SCHEMA, debug=True))
