from flask import *

app = Flask(__name__)

from view import *

if __name__ == "__main__":
    app.run(debug=True)