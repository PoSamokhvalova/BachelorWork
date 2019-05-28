from flask import Flask, render_template, request, Response
import json
from random import randint
import data_helpers

app = Flask(__name__)


@app.route('/')
def show_main_page():

    clist = ['AE','BE','BH','CA','CH','IE','SA']

    return render_template('text.html', countries=clist)


@app.route('/price', methods=['POST'])
def calculate_price():
    selected_country = request.json['country']
    print(selected_country)
    data = {
        'price': data_helpers.calculate_neo4j_price(country=selected_country)
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run()
