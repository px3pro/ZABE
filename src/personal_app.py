from flask import Flask, render_template
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)

@app.route('/')
def health_dashboard():
    return render_template('health.html', suggestion="Drink water at 8 AM")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)