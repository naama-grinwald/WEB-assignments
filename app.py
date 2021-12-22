from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = '123'

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


if __name__ == '__main__':
    app.run(debug=True)
