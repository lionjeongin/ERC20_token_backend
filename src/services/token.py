from src.token import Token

token = Token("camera unaware proud defense toe organ pull cross mobile reform buzz forward")

def get_balance(address: str):
    value = token.balanceOf(address)
    return value


def transfer(to, value):
    tx_hash = token.transfer(to, value)
    return tx_hash