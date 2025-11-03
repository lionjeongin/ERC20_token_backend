from flask import Flask, make_response
from src.token import Token

app = Flask(__name__)

@app.route("/health", methods=["POST", "GET"])
def health():
    return make_response("it's healthy", 200)

# mission 1: implement [get balance]
# - GET /token/{address}
#   - parameter: {address}: address
# - Response
#   - 200
#   - {"balance": <int>}

@app.route("/token/<address>", methods=["GET"])
def get_balance(address):
    token = Token("camera unaware proud defense toe organ pull cross mobile reform buzz forward")
    value = token.balanceOf(address)
    resp = {
        "balance": value
    }
    return make_response(resp, 200)

# mission 2: implement send
# - POST
# - /token/transfer
# - body: {"to": <address>, "value": <int>}
# - Response
#   - 200
#   - {"tx_hash": <string>}


if __name__ == "__main__":
    app.run("0.0.0.0", 5050)
