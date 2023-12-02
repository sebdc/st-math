from flask import Flask, render_template, jsonify, request
from python.midpoint import MidPoint
import os

'''
    Setting Up Flask:
        python -m venv venv
        .\venv\Scripts\activate

    For Visual Studio Code:
        ctrl + shift + p pick "Choose Interpreter"
        pick one with .\venv

    Terminal:
        python -m pip install --upgrade pip
        python -m pip install flask, sympy, numpy, matplotlib

    Run:
        flask --app app.py --debug run
'''

app = Flask(__name__)

# Main page
@app.route("/")
def home():
    return render_template('main.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Parse data from POST request
        data = request.get_json()
        f = data['functionValue']
        a = data['lowerBoundValue']
        b = data['upperBoundValue']
        n = data['subIntervalValue']

        # Remove the existing plot.png file if it exists
        plot_path = "static/plot.png"
        if os.path.exists(plot_path):
            os.remove(plot_path)

        print( f"f = {f}\n a = {a}\n, b = {b}\n, n = {n}\n" )
        midpoint = MidPoint(f,a,b,n)
        midpoint.calculateAndPlot()

        return({ "message": "success"}), 200
    except( KeyError, ValueError) as e:
        return jsonify({ "error": f"Invalid input data; {str(e)}"}), 400

if __name__ == '__main__':
    app.run(debug=True)