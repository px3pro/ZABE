import sys
import os
from flask import Flask, render_template

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import main as main_module  # Import from src directory

app = Flask(__name__)

@app.route('/')
def show_dashboard():
    # Get data from main.py
    output = []
    import io
    import sys
    sys.stdout = io.StringIO()
    main_module.orchestrate_zabe()
    output = sys.stdout.getvalue().split('\n')
    sys.stdout = sys.__stdout__
    return render_template('dashboard.html', outputs=output)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)