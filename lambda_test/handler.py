from mangum import Mangum
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route


async def homepage(request):
    response = PlainTextResponse("Hello, world!")

    return response


app = Starlette(debug=True, routes=[Route("/", homepage)])

handler = Mangum(app)
