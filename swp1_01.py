from wsgiref.simple_server import make_server
from cgi import parse_qs
import json

def application(environ, start_response):
	path = environ['PATH_INFO'].split('/')
	request_body_size = int(environ.get('CONTENT_LENGTH','0'))
	request_body = environ['wsgi.input'].read(request_body_size)
	d = parse_qs(request_body)
#	d = parse_qs(environ['QUERY_STRING'])
	name = d.get('name',[''])[0]
	age = d.get('age',[''])[0]

	print('method : %s' % environ['REQUEST_METHOD'])
	print('path : %s' %repr(path))
	
	response = {'name' : name, 'age' : age}
	response_body = json.dumps(response)
	
	status = '200 OK'
	response_headers = [
		('Content-Type','application/json'),
		('Content-Length', str(len(response_body)))
	]

	start_response(status, response_headers)
	return [response_body]


httpd = make_server('localhost',8051,application)

httpd.serve_forever()
