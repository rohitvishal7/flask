from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)
news = {"sports":"sachin retired","politics":"Modi sarkaar","academics":"Harvard Hiring"}

@app.route('/login',methods = ['POST'])
def login():
   if request.method == 'POST':
      user = request.form['username']
      if user=='mohit':
         return render_template('user.html',news=news )
      else:
         return "invalid Credentials"

@app.route('/login_redirect',methods = ['POST'])
def login_redirect():
         return render_template('login.html')



@app.route("/")
def index():
   return render_template("home.html")


if __name__ == '__main__':
   app.run(debug = True)


def hello_name(user):
    return render_template('hello.html', name=user)