# Самый простой http сервер для раздачи файлов из указанного каталога

import http.server
import socketserver
import os

PORT = 88

web_dir = os.path.join(os.path.dirname(__file__), 'web')
# os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()