

from wsgiref.simple_server import make_server
from hello import application


httpd = make_server('', 6060, application)
print 'serving http on port 6060'
httpd.serve_forever()
