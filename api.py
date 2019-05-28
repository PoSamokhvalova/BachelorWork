from flask import Flask, render_template, request, Response
import json
import data_helpers

app = Flask(__name__)


@app.route('/')
def show_main_page():

    clist = ["AdMob","Advertising whale",'AET','AEIndustries','Agile Mobile','ALT Services','Ammo','AppGen','Appss','BCA','CodiProf','Dextra','Doom','Dukes','GenerationM','GenMob','KeyMarketing','MatriX','MobileKeyServices','Mobiller','Mobistar','Mobonobe','Mobster','Newlight','Neostar','Optiserv','Place4','Proddev','Production melon','Prodster','Quantum mobile','QXZ','RatioAdv','Refcord','RingRang','ServTech','Simone Well','Victory Development','VMessage','XTF sms']

    return render_template('text.html', companies=clist)


@app.route('/price', methods=['POST', 'GET'])
def calculate_price():

    selected_country = "AE"

    data = {

        'price': data_helpers.calculate_neo4j_price(country=selected_country)

    }

    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run()
