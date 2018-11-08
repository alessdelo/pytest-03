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

# ------------------------------------

# PASS VALUES FROM QUERY STRING (request module)
# from:   https://scotch.io/bar-talk/processing-incoming-request-data-in-flask
# for testing:  https://firstpytest.herokuapp.com/query-example?language=Python&framework=Flask&website=Scotch
@app.route('/query-example')
def query_example():
    language = request.args.get('language') #if key doesn't exist, returns None
    framework = request.args['framework'] #if key doesn't exist, returns a 400, bad request error
    website = request.args.get('website')

    return '''<h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}'''.format(language, framework, website)

# ------------------------------------

# PASS VALUES FROM A FORM (request module)
# from:   https://scotch.io/bar-talk/processing-incoming-request-data-in-flask
# for testing:  https://firstpytest.herokuapp.com//form-example
@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        language = request.form.get('language')
        framework = request.form['framework']

        return '''<h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

# ------------------------------------

@app.route('/json-example')
def json_example():
    return 'Todo...'

if __name__ == '__main__':
    # Get required port, default to 5000.
    port = os.environ.get('PORT', 5000)

    # Run the app.
    app.run(host='0.0.0.0', port=port)
