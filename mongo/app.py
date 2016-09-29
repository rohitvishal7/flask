from mongoengine import *
from flask import Flask, request, flash, url_for, redirect, render_template
app = Flask(__name__)

connect('test')


class add_blog(Document):
    name_of_blog = StringField(required=True)
    content = StringField(max_length=500)
    author = StringField(max_length=50)
    image =  StringField(max_length=100)



class add_comment(Document):
    name = StringField(required=True)
    comment = StringField(max_length=200)


@app.route('/')
def show_all():
    return render_template('mohitWriteBlog.html')


@app.route('/add_blog', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        ross = add_blog(name_of_blog=request.form['name'],
                    content=request.form['content'],
                    author=request.form['author'],
                    image=request.form['image']
                    ).save()
        return render_template("index.html")



@app.route('/add_comment', methods=['GET', 'POST'])
def new1():
    if request.method == 'POST':
        ross = add_comment(name=request.form['name'],
                    comment=request.form['comment'],
                    ).save()



@app.route('/show_blogs')
def show():
    query=add_blog.objects()
    return render_template("index.html",query=query)


if __name__ == '__main__':
    app.run(debug=True)
