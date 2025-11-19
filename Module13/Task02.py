from flask import Flask, request
from flask_cors import CORS
import mysql.connector

connection = mysql.connector.connect(
    host='mysql.metropolia.fi',
    port=3306,
    database='mydatabase',
    user='root',
    password='27111997',
    autocommit=True
)

def get_airport_by_icao_code(icao_code):
    sql = "SELECT * FROM airport WHERE ident='{icao_code}'"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchone()
    print('Debug', result)
    return result

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/airport/<icao>')
def get_airport(icao):
    try:
        airport =  get_airport_by_icao_code(icao)
        if airport == None:
            return {'error': 'Airport not found'}, 404
        return airport
    except Exception:
        return {'message': 'Something went wrong'}, 500


if __name__ == '__main__':
    app.run(use_reloader=True, host='localhost', port=3000)