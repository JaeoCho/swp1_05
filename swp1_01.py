from wsgiref.simple_server import make_server
from cgi import parse_qs

def application(environ, start_response):

	d = parse_qs(environ['QUERY_STRING'])
	name = d.get('name',[''])[0]
	age = d.get('age',[''])[0]

	response_body = 'name : %s\nage : %s\n' %(name,age)
	
	status = '200 OK'
	response_headers = [
		('Content-Type','text/plain'),
		('Content-Length', str(len(response_body)))
	]

	start_response(status, response_headers)
	return [response_body]


httpd = make_server('localhost',8051,application)

httpd.serve_forever()
