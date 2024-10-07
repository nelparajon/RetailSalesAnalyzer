from flask import Flask, send_file
from load_data import load_data
import process_data
import data_visualyzer as dv
from io import BytesIO

app = Flask(__name__)

@app.route('/total_amount_by_cat', methods=['GET'])
def total_amount_by_cat():
    data = load_data()
    df = process_data.total_amount_by_category(data)
    img = dv.visualyze_total_amount_by_cat(df)
    
    return send_file(img, mimetype='image/png')

@app.route('/total_amount_by_month', methods=['GET'])
def total_amount_by_month():
    data = load_data()
    df = process_data.total_amount_by_month(data)
    img = dv.visualyze_total_amount_by_month(df)
    
    return send_file(img, mimetype='image/png')

@app.route('/percent_amount_by_month', methods=['GET'])
def percent_amount_by_month():
    data = load_data()
    df = process_data.porcentaje_compras_cat_month(data)
    img = dv.percent_amount_by_month(df)
    
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
