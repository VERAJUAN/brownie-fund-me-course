from brownie import FundMe
from scripts.helpful_scripts import get_account, get_verify, get_network, get_price_feed_address, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def deploy_fund_me():
    print(get_network())
    if(get_network() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS):
        price_feed_address = get_price_feed_address()
    else:
        price_feed_address = deploy_mocks()

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": get_account()},
        publish_source=get_verify()
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()

