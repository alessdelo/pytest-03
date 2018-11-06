import os
from bottle import route, run

@route('/')


@route('/hello/:name')
def index(name='World'):
    add_string = '<b>Hello %s!</b>' % name



    
a=1+1
b=2+2

    
mystring = '''<html>
<head><title>My first Python CGI app</title></head>
<body>'''

mystring += '<p>Bla, Bla, Bla.....</p>'

mystring += add_string

mystring += '</body></html>'

mystring

if __name__ == '__main__':
    # Get required port, default to 5000.
    port = os.environ.get('PORT', 5000)

    # Run the app.
    run(host='0.0.0.0', port=port)
