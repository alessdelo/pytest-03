# test

import os

from flask import Flask, request, render_template, url_for
from forms import RegistrationForm, LoginForm
from flask_wtf.csrf import CSRFProtect
from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['SECRET_KEY'], os.environ['WTF_CSRF_SECRET_KEY'])

# creates an instance of Flask class
app = Flask(__name__)
CSRFProtect(app)

# secret_key = os.environ.get('SECRET_KEY')
# csrf_secret_key = os.environ.get('WTF_CSRF_SECRET_KEY')
        
# some dummy data...
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


# ------------------------------------

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', posts=posts)

# ------------------------------------

@app.route('/about')
def about():
    return render_template('about.html', title='About', secret_key = (s3[0], s3[1])

# ------------------------------------

@app.route('/register', methods=['GET' , 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


# ------------------------------------

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

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
# for testing:  https://firstpytest.herokuapp.com/form-example
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

@app.route('/json-example', methods=['POST']) #GET requests will be blocked
def json_example():
    req_data = request.get_json()

    language = req_data['language']
    framework = req_data['framework']
    python_version = req_data['version_info']['python'] #two keys are needed because of the nested object
    example = req_data['examples'][0] #an index is needed because of the array
    boolean_test = req_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)


# ------------------------------------

if __name__ == '__main__':
    # Get required port, default to 5000.
    port = os.environ.get('PORT', 5000)

    # Run the app.
    app.run(host='0.0.0.0', port=port)
