from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response('200 OK', [('Content-Type','text/plain')])
    yield 'Hello World\n'


httpd = make_server('localhost',8051,application)

httpd.handle_request()