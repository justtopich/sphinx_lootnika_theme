"""
In sphinx.cmd.build you need change this

    # if __name__ == '__main__':
    #     sys.exit(main(sys.argv[1:]))
    if __name__ != '__main__':
        main(sys.argv[1:])

"""
import sys
import shutil
import asyncio
import logging
from os import makedirs
from aiohttp import web


sys.argv.append('-M')
sys.argv.append('html')
sys.argv.append('D:\pydev\pet\lootnika.docs\source')
sys.argv.append('D:\pydev\pet\lootnika.docs\\build')

try:
    shutil.rmtree('D:\pydev\pet\lootnika.docs\\build')
except Exception as e:
    print(e)

try:
    makedirs('D:\pydev\pet\lootnika.docs\\build\html')
except:
    pass

from sphinx.cmd import build

PORT = 8000
URL = '/help'
ADDRESS = "127.0.0.1"
DIRECTORY = 'D:\pydev\pet\lootnika.docs\\build\\html'
routes = web.RouteTableDef()

console = logging.StreamHandler(stream=sys.stdout)  # вывод в основной поток
logRest = logging.getLogger('RestServer')
logRest.setLevel(logging.INFO)
logRest.addHandler(console)


async def start_server():
    try:
        runner = web.AppRunner(
            app,
            handle_signals=False,
            access_log = logRest,
            access_log_format='%a %s "%r" "%{Referer}i"'
        )
        await runner.setup()
        srv = web.TCPSite(runner, ADDRESS, PORT)
        await srv.start()

        print(f"Started at {ADDRESS}:{PORT}{URL}")
        while True:
            await asyncio.sleep(3600)

    except Exception as e:
        print(e)




@routes.get('/help/')
async def handle(request):
    return web.FileResponse(f'{DIRECTORY}/index.html')

@routes.get('/')
async def handle(request):
    raise web.HTTPFound('/help/')

routes.static(f"{URL}", DIRECTORY)
app = web.Application()
app.add_routes(routes)

loop = asyncio.get_event_loop()

loop.run_until_complete(start_server())
