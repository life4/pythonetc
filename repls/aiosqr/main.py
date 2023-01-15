import aiohttp
from aiohttp import web
import asyncio


class Queue:
    _INSTANCE = None

    def __init__(self):
        self._cache = {}
        asyncio.get_event_loop().create_task(self._process())

    @classmethod
    def instance(cls):
        if cls._INSTANCE is None:
            cls._INSTANCE = cls()

        return cls._INSTANCE

    def add(self, future, i):
        self._cache[i] = future

    async def _process(self):
        while True:
            await asyncio.sleep(1)
            old_cache = self._cache
            self._cache = {}
            query = list(old_cache.keys())
            async with aiohttp.ClientSession() as session:
                async with session.post('http://localhost:8080/', json=query) as response:
                    result = await response.json()
                    for index, value in enumerate(query):
                        old_cache[value].set_result(result[index])


async def sqr(i):
    future = asyncio.get_event_loop().create_future()
    Queue.instance().add(future, i)
    return await future


async def sqr_and_print(i):
    result = await sqr(i)
    print(result)


async def sqr_all():
    i = 0
    while True:
        i += 1
        asyncio.ensure_future(sqr_and_print(i))
        await asyncio.sleep(0.3)


async def client(app):
    asyncio.ensure_future(sqr_all())


routes = web.RouteTableDef()


@routes.post('/')
async def sqr_route_post(request):
    data = await request.json()
    return web.json_response([x ** 2 for x in data])


@routes.get('/')
async def sqr_route_get(request):
    return web.Response(text='http://t.me/pythonetc')


def main():
    app = web.Application()
    app.on_startup.append(client)
    app.add_routes(routes)
    web.run_app(app)


if __name__ == '__main__':
    main()
