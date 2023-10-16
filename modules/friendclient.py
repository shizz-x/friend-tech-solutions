import web3 as WEB3
import os
import asyncio
from consts.abi import FRIEND_TECH_SHARES_ADDRES, FRIEND_TECH_SHARES_ABI

web3_base = WEB3.Web3(WEB3.HTTPProvider(os.environ['base_http_uri']))
shares_contract = web3_base.eth.contract(address=FRIEND_TECH_SHARES_ADDRES, abi=FRIEND_TECH_SHARES_ABI)

class Client:
    wallet: WEB3.Account
    def __init__(self, private_key: str) -> None:
        self.__private_key = private_key
        self.wallet = WEB3.Account.from_key(self.__private_key)
        self.base_balance = self._get_balance(self.wallet.address)
    
    def _get_balance(self, address:str):
        return web3_base.eth.get_balance(address)
    
    def _fees_precents(self):
        return shares_contract.functions.protocolFeePercent().call(), shares_contract.functions.subjectFeePercent().call()
    
    async def _get_key_buy_price(self, address: str):
        return shares_contract.functions.getBuyPrice(address, 1).call()
    
    async def _get_key_sell_price(self, address: str):
        return shares_contract.functions.getSellPrice(address, 1).call()
    
    async def _get_key_base_price(self, supply: int):
        return shares_contract.functions.getPrice(supply, 1).call()
    
    async def _get_key_buy_price_after_fee(self, supply: int):
        return shares_contract.functions.getBuyPriceAfterFee(supply, 1).call()
    
    async def _get_key_sell_price_after_fee(self, supply: int):
        return shares_contract.functions.getSellPriceAfterFee(supply, 1).call()
    
    async def buy_key(self, address: str):
        value = await self._get_key_buy_price_after_fee(address)

        transaction = shares_contract.functions.buyShares(address, 1).build_transaction({
            'from': self.wallet.address,
            'value': value,
            'nonce': web3_base.eth.get_transaction_count(self.wallet.address),
        })

        signed_transaction = self.wallet.sign_transaction(transaction)

        hash = web3_base.eth.send_raw_transaction(signed_transaction.rawTransaction)

        return hash
    
    async def sell_key(self, address: str):
        
        transaction = shares_contract.functions.sellShares(address, 1).build_transaction({
            'from': self.wallet.address,
            'value': 0,
            'nonce': web3_base.eth.get_transaction_count(self.wallet.address),
        })

        signed_transaction = self.wallet.sign_transaction(transaction)

        hash = web3_base.eth.send_raw_transaction(signed_transaction.rawTransaction)

        return hash
    
    
        

