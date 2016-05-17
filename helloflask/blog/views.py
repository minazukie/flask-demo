# coding:utf-8
import math

import time

import random
from flask import render_template, flash, redirect, request, session
from blog import blog
from blog.forms import LoginForm
from blog.sql import *


@blog.route('/')
def helloworld():
    return redirect('/index')


@blog.route('/index')
def index():
    if request.args.get('page', '1'):
        page = int(request.args.get('page', '1'))
    else:
        page = 1
    posts = sql_dict(paginate(page))
    total = sql_dict(all_blog())
    count = 0
    for c in total:
        count += 1
    count = count / 5.0
    count = int(math.ceil(count))
    category = sql_dict(countcategory())
    print(category)
    return render_template("index.html",
                           title='Sandwinds',
                           user="user",
                           posts=posts,
                           category=category,
                           count=count,
                           page=page)


@blog.route('/category/<tag>')
def categorys(tag):
    posts = sql_dict(getcategory(tag))
    if (posts):
        count = 0
        page = 1
        category = sql_dict(countcategory())
        return render_template("index.html",
                               title=tag,
                               user="tag",
                               posts=posts,
                               category=category,
                               count=count,
                               page=page)
    else:
        return render_template("404.html", )


@blog.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html',
                           title='ABOUT',
                           )


@blog.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for Name: ' + form.name.data)
        flash('passwd: ' + str(form.password.data))
        flash('remember_me: ' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)


@blog.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        print(request.form['id'])
        print(searchById(request.form['id']))
        posts = sql_dict(searchById(request.form['id']))
    return render_template("search.html", title='Home',
                           user="user",
                           posts=posts)


@blog.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'GET':
        if (sql(editblog(request.args.get('id'), "444")) == "done"):
            return "ok"
        else:
            print("fail")
    return "ok"


@blog.route('/detail/<b_id>', methods=['GET', 'POST'])
def detail(b_id):
    if b_id.isdigit() == True:
        print(b_id)
        print(searchById(b_id))
        comms = sql_dict(getcomm(b_id))
        posts = sql_dict(searchById(b_id))
        session['va'] = random.randint(0, 10)
        session['vb'] = random.randint(0, 10)
        session['vah'] = numtohan(session['va'])
        session['vbh'] = numtohan(session['vb'])
        print(session['va'] * session['vb'])
        if 'nickname' in session:
            nickname = session['nickname']
        else:
            nickname = ""
    else:
        return "Error"
    return render_template("detail.html",
                           posts=posts,
                           comms=comms,
                           nickname=nickname,
                           b_id=b_id
                           )


@blog.route('/signin', methods=['POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = sql_dict(verifylogin(username, password))
        if (verify):
            session['username'] = request.form['username']
            return "yes"
        else:
            return "no"
    return render_template("404.html",
                           )


@blog.route('/signout', methods=['POST'])
def signout():
    if request.method == 'POST':
        session.pop('username', None)
    return redirect('/index')


@blog.route('/admin', methods=['POST'])
def admin():
    if request.method == 'POST':
        if 'username' in session:
            return render_template("admin.html",
                                   )
        else:
            return render_template("404.html",
                                   )


@blog.route('/blogpost', methods=['POST'])
def blogpost():
    if request.method == 'POST':
        if 'username' in session:
            if (sql(newblog(request.form['title'], request.form['tag'], request.form['pre'],
                            request.form['text'])) == "done"):
                return "yes"
            else:
                return "no"
        else:
            return "no";
    else:
        return render_template("404.html",
                               )


@blog.route('/commpost', methods=['POST'])
def commpost():
    if request.method == 'POST':
        if request.form['name'] == "羽崎水无月":
            flash(u"很遗憾，失败了")
            return redirect('/detail/' + request.form['b_id'])
        else:
            if request.form['name'] == "174I-044L-522Y":
                if (sql(newcomm("羽崎水无月", request.form['text'], request.form['email'], request.form['b_id'])) == "done"):
                    return redirect('/detail/' + request.form['b_id'])
                else:
                    return render_template("404.html",
                                           )
            else:
                if int(request.form['vc']) == session['va'] * session['vb']:
                    if (sql(newcomm(request.form['name'], request.form['text'], request.form['email'],
                                    request.form['b_id'])) == "done"):
                        session['nickname'] = request.form['name']
                        return redirect('/detail/' + request.form['b_id'])
                    else:
                        return render_template("404.html",
                                               )
                else:
                    flash(u"验证码错误")
                    return redirect('/detail/' + request.form['b_id'])


@blog.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@blog.errorhandler(405)
def page_not_allowed(error):
    return render_template('404.html'), 405


@blog.errorhandler(500)
def page_not_allowed(error):
    return render_template('500.html'), 500


def numtohan(id):
    dict = {0: "零", 1: "一", 2: "二", 3: "三", 4: "四", 5: "五", 6: "六", 7: "七", 8: "八", 9: "九", 10: "十"}
    return dict[id]
