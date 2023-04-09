from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from methods.facebook import get_facebook
from methods.amazon import get_amazon
from methods.flipkart import get_flipkart
from methods.swiggy import get_swiggy
from methods.revv import get_revv
from methods.whatsapp import get_whatsapp
from methods.ola import get_ola


app = Flask(__name__, template_folder='templates')
# CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    return render_template("index.html")

@app.route('/get_data', methods=['GET', 'POST'])
def get_data():
    user_input = request.form.get('email')
    if user_input.isnumeric():
        # try:
            whatsapp = get_whatsapp(user_input)
            swiggy = get_swiggy(user_input)
            ola = get_ola(user_input)
            
            return render_template('index.html',swiggy=swiggy,ola=ola,whatsapp=whatsapp)
        # except:
        #     swiggy = get_swiggy(user_input)
        #     ola = get_ola(user_input)
        # return render_template('index.html',swiggy=swiggy,ola=ola)
    else:
        revv = get_revv(user_input)
        facebook = get_facebook(user_input)
        amazon = get_amazon(user_input)
        flipkart = get_flipkart(user_input)       
        return render_template('index.html',facebook=facebook,amazon=amazon,flipkart=flipkart,revv=revv)
        

if __name__ == "__main__":
    app.run()
