
from flask import Flask, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'

@app.route("/")
def home():
    
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

  
    files = os.listdir(UPLOAD_FOLDER)

    return render_template("index.html", files=files)
app.run(debug=True, use_reloader=False)
if __name__ == '__main__':
    app = Flask(__name__)






