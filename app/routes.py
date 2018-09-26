# -*- coding: future_fstrings -*-
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import PostForm, DeleteForm
import pymysql
from datetime import datetime

IP = '35.197.193.248'
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
	c.execute(f"insert into tbl_posts values('{name}','{post}','{date}')")
	db.commit()
	return redirect(url_for('forum'))
    return render_template('index.html', title='Home', form=form)

@app.route('/forum')
def forum():
    c.execute(f"SELECT * FROM tbl_posts")
    s = "<table style='border:1px solid black'>"  
    for row in c:  
    	s = s + "<tr>"  
    	for x in row:  
    		s = s + "<td>" + str(x) + "</td>"  
    s = s + "</tr>" 
    p = "<html><body>" + s + "</body></html>"
    #return p
     
    return render_template('forum.html', title='Forum', posts=p)

@app.route('/delete', methods=['GET','POST'])
def delete():
    form = DeleteForm()
    id = form.id.data
    if form.validate_on_submit():
	c.execute(f"DELETE FROM tbl_posts WHERE id={id}")
	db.commit()
	flash("Successfully deleted Post {}").format(id)
        return redirect(url_for('forum'))
    return render_template('delete.html', title='Forum', form=form)

