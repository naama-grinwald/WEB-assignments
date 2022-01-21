from random import random

from flask import Flask, redirect, url_for, render_template, request, session, jsonify
import requests

from pages.assignment10.interact_with_DB import interact_db

app = Flask(__name__)
app.secret_key = '1234'


from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)


@app.route('/home')
@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/about')
def about_func():
    return render_template('about.html')


@app.route('/skills')
@app.route('/assignment8')
def assignment8_func():
    return render_template('assignment8.html',
                           languages=['SQL', 'R', 'Python', 'Java', 'VBA', 'HTML', 'CSS', 'JavaScript'],
                           user={'firstname': 'Naama', 'lastname': 'Grinwald'}
                           )


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9_func():
    profiles = {'user1': {'name': 'Omer', 'email': 'omer@gmail.com'},
                'user2': {'name': 'Alon', 'email': 'alon@gmail.com'},
                'user3': {'name': 'Orly', 'email': 'orly@gmail.com'},
                'user4': {'name': 'Guy', 'email': 'guy@gmail.com'},
                'user5': {'name': 'Naama', 'email': 'naama@gmail.com'}}

    if request.method == 'GET':
        if 'search' in request.args:
            if request.args.get('s_userkey') !='':
                s_userkey = request.args['s_userkey']
                for key in profiles:
                    if key==s_userkey:
                        s_username=profiles[key]['name']
                        s_email=profiles[key]['email']
                        return render_template('assignment9.html', username=session['username'], email=session['email'],
                                               password=session['password'], s_username=s_username, s_email=s_email)
                return render_template('assignment9.html', username=session['username'], email=session['email'],
                                               password=session['password'], nokey='nokey', s_userkey=s_userkey)

            return render_template('assignment9.html', username=session['username'], email=session['email'],
                                   password=session['password'], profiles=profiles)

        #return render_template('assignment9.html')
        return render_template('assignment9.html', username=session['username'], email=session['email'], password=session['password'])

    if request.method == 'POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']

        session['username'] = username
        session['email'] = email
        session['password'] = password
        session['user_inside'] = True

        return render_template('assignment9.html', username=username, email=email, password=password)


@app.route('/logout')
def logout_func():
    session['username']= ''
    session['email'] = ''
    session['password'] = ''
    session['user_inside'] = False

    return render_template('assignment9.html', username=session['username'], email=session['email'],
                           password=session['password'])


# assignment11
@app.route('/assignment11/users')
def assignment11_users():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    response = jsonify(query_result)
    return response


@app.route('/assignment11/outer_source', methods=['GET', 'POST'])
def assignment11_outer_source():
    return render_template('assignment11.html')


@app.route('/get_user', methods=['POST'])
def assignment11_get_user():
    id = request.form['id']
    return render_template('assignment11.html', id=id)


@app.route('/req_backend')
def req_backend_func():
    user=0
    if "user" in request.args and request.args['user']!='':
        user = request.args['user']
    res=requests.get(f'https://reqres.in/api/users/{user}')
    res = res.json()
    return render_template('assignment11.html', user=res)


@app.route('/assignment12/restapi_users', defaults={'user_id': 1})
@app.route('/assignment12/restapi_users/<int:user_id>')
def assignment12(user_id):
    query = 'select * from users where id=%s' % user_id
    users = interact_db(query=query, query_type='fetch')
    if len(users) == 0:
        return_dict = {
            'status': 'failed',
            'message': 'user not found'
        }
    else:
        return_dict = {
            'status': 'success',
            f'id': users[0].id,
            'name': users[0].name,
            'email': users[0].id,
        }
    return jsonify(return_dict)


if __name__ == '__main__':
    app.run(debug=True)
