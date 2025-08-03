from flask import Flask, render_template, requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)

@app.route('/')
def health_dashboard():
    response = requests.get('https://<api-id>.execute-api.us-east-1.amazonaws.com/prod/aggregate')
    status = response.json().get('body', 'Service active!')
    return render_template('health.html', suggestion=status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)