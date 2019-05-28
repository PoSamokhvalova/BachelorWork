from flask import Flask, render_template, request, Response
import json
from random import randint

app = Flask(__name__)


@app.route('/')
def show_main_page():

    clist = ["AdMob","Advertising whale",'AET','AEIndustries','Agile Mobile','ALT Services','Ammo','AppGen','Appss','BCA','CodiProf','Dextra','Doom','Dukes','GenerationM','GenMob','KeyMarketing','MatriX','MobileKeyServices','Mobiller','Mobistar','Mobonobe','Mobster','Newlight','Neostar','Optiserv','Place4','Proddev','Production melon','Prodster','Quantum mobile','QXZ','RatioAdv','Refcord','RingRang','ServTech','Simone Well','Victory Development','VMessage','XTF sms']

    return render_template('text.html', companies=clist)


@app.route('/price', methods=['POST'])
def calculate_price():
    data = {
        'price': randint(10, 50)
    }
    js = json.dumps(data)
    command= 'select dfgv -> njj []'
    resp = Response(js, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run()
