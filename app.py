from flask import Flask, redirect, url_for

# Make one usage of redirect() function and one usage of redirect() and url_for() functions.

app = Flask(__name__)


@app.route('/')
def home_page():
    return 'This is Home Page!'

@app.route('/about')
def about_func():
    return 'About me page!'

@app.route('/hello')
def hello_world():
    return redirect('/home')

@app.route('/home')
def home_func():
    return redirect(url_for('home_page'))

@app.route('/catalog')
def catalog_func():
    return "welcome to catalog page"

if __name__ == '__main__':
    app.run(debug=True)
