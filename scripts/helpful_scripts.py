from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = Web3.toWei(2000, "ether")
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development","ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]

def get_account():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS 
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.load("freecodecamp-account")
    
def get_verify():
    return config["networks"][get_network()].get("verify")

def get_price_feed_address():
    return config["networks"][get_network()].get("eth_usd_price_feed")

def get_network():
    return network.show_active()

def deploy_mocks():
    print(f"the active network is {get_network()}")
    print(f"Deploying the mocks!")
    MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print(f"Mocks Deployed")
    return MockV3Aggregator[-1].address
