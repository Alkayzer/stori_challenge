from flask import Flask
from routes.router import transaction_bp

app = Flask(__name__)

app.register_blueprint(transaction_bp)

if __name__ == '__main__':
    app.run(debug=True)
