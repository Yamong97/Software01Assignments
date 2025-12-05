from flask import Flask, request, Response
import mysql.connector
import json

app = Flask(__name__)
app.json.sort_keys = False

connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='27111997',
    port=3306,
    database='flight_game',
    autocommit=True,
)

def get_airport_by_icao_code(icao_code):
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (icao_code.upper(),))
    result = cursor.fetchone()
    cursor.close()
    if result:
        response = {
            "ICAO": icao_code.upper(),
            "Name": result["name"],
            "Location": result["municipality"],
        }
        print('Debug', result)
        return response
    else:
        return None

@app.route('/airport/<icao_code>', methods=['GET'])
def get_airport(icao_code):
    data = get_airport_by_icao_code(icao_code.upper())
    if data:
        return Response(json.dumps(data), mimetype='application/json')
    else:
        error_data = {"error": f"Airport not found '{icao_code.upper()}'"}
        return Response(json.dumps(error_data), status=404, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, host = "127.0.0.1", port = 5000)