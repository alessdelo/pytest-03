import os
# from bottle import route, run

from flask import Flask, request
app = Flask(__name__)

head = '''<html>
<head><title>Page 1</title></head>
<body>'''

foot = '</body></html>'


@app.route('/')
def index():
    mystring = head
    mystring += '<h1>Main Page</h1>'
    mystring +=  '<p>This is the main page...</p>'
    mystring += foot    
    return mystring

@app.route('/hello/:name')
def hello(name='World'):
    return '<b>Hello %s!</b>' % name
    
@app.route('/page1/:greet')
def page1(greet='mikey'):
    mystring = head
    mystring += '<p>Bla, Bla, Bla.....</p>'
    mystring +=  '<b>Ciao %s!</b>' % greet
    mystring += foot    
    return mystring

if __name__ == '__main__':
    # Get required port, default to 5000.
    port = os.environ.get('PORT', 5000)

    # Run the app.
    app.run(host='0.0.0.0', port=port)
