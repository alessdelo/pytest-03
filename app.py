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

@app.route('/query-example')
def query_example():
    return 'Todo...'

@app.route('/form-example')
def form_example():
    return 'Todo...'

@app.route('/json-example')
def json_example():
    return 'Todo...'

if __name__ == '__main__':
    # Get required port, default to 5000.
    port = os.environ.get('PORT', 5000)

    # Run the app.
    app.run(host='0.0.0.0', port=port)
