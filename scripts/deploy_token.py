from brownie import OurToken
from scripts.utils import get_account

# 5000 * 10^18; for decimal value is 18
INITIAL_SUPPLY = 500000000000000000000


def deploy_token():
    account = get_account()
    token = OurToken.deploy(INITIAL_SUPPLY, {"from": account})
    print(token.name())
    print("token is generated!")


def main():
    deploy_token()
