from aiohttp import ClientSession
from consts.headers import PARSER_HEADERS


class Parser:
    proxies: list[str] | None
    index_of_proxy: int
    api_domain: str
    get_online_users_endpoint: str
    headers: dict

    @property
    def proxy(self) -> str | None:
        if self.proxies is None:
            return None
        proxy = self.prepare_proxy(self.proxies[self.index_of_proxy])
        self.index_of_proxy += 1
        if self.index_of_proxy == len(self.proxies):
            self.index_of_proxy = 0
        return proxy

    def __init__(self, proxies: list[str] | None = None):
        if proxies is not None:
            for proxy in proxies:
                self.prepare_proxy(proxy)
        self.proxies = proxies
        self.index_of_proxy = 0
        self.api_domain = 'https://prod-api.kosetto.com/'
        self.get_online_users_endpoint = 'lists/online'
        self.headers = PARSER_HEADERS.copy()

    async def get_online_users(self) -> list[any]:
        """
        returns list of users from https://prod-api.kosetto.com/lists/online
        """
        async with ClientSession(headers=self.headers) as session:
            async with session.get(self.api_domain + self.get_online_users_endpoint, proxy=self.proxy) as response:
                data = dict(await response.json(encoding='UTF-8'))
                return list(data.get('users'))

    @staticmethod
    def prepare_proxy(proxy_string):
        if proxy_string is None:
            return None

        PROXY_HOST = ''
        PROXY_PORT = ''
        PROXY_USER = ''
        PROXY_PASS = ''

        if ':' in proxy_string:
            components = proxy_string.split(':')
            if len(components) == 4:
                PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS = components
            elif len(components) == 2:
                PROXY_HOST, PROXY_PORT = components
            else:
                raise ValueError(
                    "Прокси не соответствует ожидаемому формату: 'host:port:user:password' или 'host:port'")
        else:
            PROXY_HOST = proxy_string

        return f'http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}'
