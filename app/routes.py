# -*- coding: future_fstrings -*-
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import PostForm, DeleteForm, UpdateForm
import pymysql
from datetime import datetime

IP = '35.197.215.110'
U = 'root'
P = 'password'
dbname = "Bucketlist"
db = pymysql.connect(IP,U,P,dbname)
c = db.cursor()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PostForm()
    name = form.name.data
    post = form.post.data
    datetm = datetime.now()
    date = datetm.strftime("%Y-%m-%d")
    if form.validate_on_submit():
        post = post.replace("'", "\\'")
	c.execute(f"insert into tbl_posts (name, posts, datetime) values('{name}','{post}','{date}')")
	db.commit()
	return redirect(url_for('forum'))
    return render_template('index.html', title='Home', form=form)

@app.route('/forum')
def forum():
    c.execute(f"SELECT * FROM tbl_posts")
    base = f"<html><head><title>QA FORUM</title></head><body><div>QA Forum: <a href=\"/index\">Home</a> <a href=\"/forum\">Forum</a> <a href=\"/delete\">Delete</a> <a href=\"/update\">Update</a></div>"

    s = base + "<h1>Welcome to QA Forum!</h1><h1>These are the posts!</h1><table style='border:1px solid black'>"  
    for row in c:  
    	s = s + "<tr>"  
    	for x in row:  
    		s = s + "<td>" + str(x) + "</td>"  
    s = s + "</tr>" 
    p = s + "</body></html>"
    return p 
     
@app.route('/delete', methods=['GET','POST'])
def delete():
    form = DeleteForm()
    id = form.id.data
    if form.validate_on_submit():
	c.execute(f"DELETE FROM tbl_posts WHERE user_id={id}")
	db.commit()
	flash("Successfully deleted Post")
        return redirect(url_for('forum'))
    return render_template('delete.html', title='Delete', form=form)

@app.route('/update', methods=['GET', 'POST'])
def update():
    form = UpdateForm()
    id = form.id.data
    datetm = datetime.now()
    date = datetm.strftime("%Y-%m-%d")
    post = form.post.data
    if form.validate_on_submit():
	post = post.replace("'", "\\'")
	c.execute(f"UPDATE tbl_posts SET posts='{post}', datetime='{date}' WHERE user_id='{id}'")
	return redirect(url_for('forum'))
    return render_template('update.html', title='Update', form=form)


