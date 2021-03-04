#! /usr/bin/python

from flask import Flask,render_template,url_for,request,redirect,jsonify
import logging
import datetime
import locale
from bdd import Mybdd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wiki')
def wiki():
    result_dict = []
    cursor = mybdd.cursor()
    sql = "SELECT * FROM articles" 
    cursor.execute(sql)
    app.logger.info('%s Database successfully connected')
    # for res in cursor:
    #     result_dict.append({'id':res['id'],'title':res['title'], 'images':res['image'], 'content':res['content'], 'date':res['date']})
    results = cursor.fetchall()
    app.logger.info('%s database successfully filled')
    print(results)
    # return jsonify(result_dict)
    return render_template('index.html',len=len(results))
    

# @app.route('/mail')
# def mailing():



@app.route('/login', methods=['POST'])
def login():
    user = get_user(request.form['username'])

    if user.check_password(request.form['password']):
        login_user(user)
        app.logger.info('%s logged in successfully', user.username)
        return redirect(url_for('index'))
    else:
        app.logger.info('%s failed to log in', user.username)
        abort(401)

if __name__ == "__main__":
    app.run( port= 5000,debug=True)