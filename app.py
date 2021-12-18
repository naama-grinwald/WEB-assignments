from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/about')
def about_func():
    return render_template('about.html')


@app.route('/contact')
def contact_func():
    return render_template('contact.html')


@app.route('/skills')
@app.route('/assignment8')
def assignment8_func():
    return render_template('assignment8.html',
                           languages=['SQL', 'R', 'Python', 'Java', 'VBA', 'HTML', 'CSS', 'JavaScript'],
                           user={'firstname': 'Naama', 'lastname': 'Grinwald'}
                            )


if __name__ == '__main__':
    app.run(debug=True)
