from modules.friendtechparser import Parser
from modules.friendclient import Client
from modules.utils import Utility
import asyncio
class Core:


    @property
    def parser(self) -> Parser:
        return self.__parser

    def __init__(self) -> None:
        self.__parser = Parser(Utility.get_proxies())
        self._friend_clients = [Client(key) for key in Utility.get_keys()]



    def start_procces(self):
        asyncio.run(self.loop())
        
    async def loop(self) -> None:
        
        for client in self._friend_clients:
            
            print(await self.parser.get_online_users())
            print(client.wallet.address)
            print(client.base_balance)
            print(await client.buy_key(client.wallet.address))
            print(await client.sell_key(client.wallet.address))
    
    


            
            




