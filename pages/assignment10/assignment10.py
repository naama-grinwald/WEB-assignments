from flask import Blueprint, render_template, redirect, flash
from pages.assignment10.interact_with_DB import interact_db
from flask import request

# Assignment10 blueprint definition
assignment10 = Blueprint('assignment10', __name__,
                static_folder='static',
                static_url_path='/pages/assignment10',
                template_folder='templates')


# Routes
@assignment10.route('/assignment10', methods=['GET', 'POST'])
def assignment10_func():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=users)


@assignment10.route('/insert_user', methods=['POST'])
def insert_user_func():
    # get data
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    # insert to DB
    query = "INSERT INTO users(name, email, password) VALUES ('%s', '%s', '%s')" % (name,email,password)
    interact_db(query=query, query_type='commit')

    # back to users
    return redirect('/assignment10')

@assignment10.route('/update_user', methods=['POST'])
def update_user_func():
    id = request.form['id']
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    query = "select * FROM users WHERE id = '%s';" % id
    query_result = interact_db(query=query, query_type='fetch')
    if len(query_result) > 0:
        query = "UPDATE users SET name='%s', email='%s', password='%s' WHERE id = '%s';" % (name,email,password, id)
        interact_db(query=query, query_type='commit')
        flash(f'User {id} update successfuly!')
        return redirect('/assignment10')
    else:
        flash(f'User {id} does not exist, update wasnt made')
        return redirect('/assignment10')


@assignment10.route('/delete_user', methods=['POST'])
def delete_user_func():
    id = request.form['id']

    query = "select * FROM users WHERE id = '%s';" % id
    query_result = interact_db(query=query, query_type='fetch')
    if len(query_result) > 0:
        query = "DELETE FROM users WHERE id='%s';" % id
        interact_db(query=query, query_type='commit')
        flash(f'User {id} deleted successfuly!')
        return redirect('/assignment10')
    else:
        flash(f'User {id} does not exist, delete wasnt made')
        return redirect('/assignment10')
