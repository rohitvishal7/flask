from flask import Flask, render_template,request,redirect,url_for,make_response,session



app = Flask(__name__)
app.secret_key = 'any random string'
cart=[]

cars={"/static/1.jpg":[1,'merc', 4000,"available"],"/static/2.jpg":[2,'bmw', 5000,"available"],"/static/3.jpg":[3,'rr', 8000,"available"]}
bikes={"/static/8.jpg":[1,'merc', 4000,"available"],"/static/78.png":[2,'bmw', 5000,"available"],"/static/88.jpg":[3,'rr', 8000,"available"]}
fur={"/static/1.jpg":[1,'merc', 4000,"available"],"/static/2.jpg":[2,'bmw', 5000,"available"],"/static/3.jpg":[3,'rr', 8000,"available"]}
home={"/static/4.jpg":[1,'merc', 4000,"available"],"/static/5.jpg":[2,'bmw', 5000,"available"],"/static/6.jpg":[3,'rr', 8000,"available"]}
@app.route("/")
def index():
    if 'username' in session:
        username = session['username']
    return render_template("index.html")

@app.route('/car')
def car():
          return render_template("cars.html",cars=cars)

@app.route('/bikes')
def bikes():
          return render_template("bikes.html",bikes=bikes)


@app.route('/fur')
def Furniture():
          return render_template("fur.html",fur=fur)


@app.route('/homes')
def Homes():
          return render_template("home.html",home=home)

@app.route('/addToCart/<value>')
def addToCart(value):

    global cart
    cart.append(value)
    session['cart'] =cart
    return render_template('index.html')

@app.route('/showCart')
def showCart():
    data=session['cart']
    return render_template('show.html',cart=data)















if __name__ == '__main__':
   app.run(debug = True)


