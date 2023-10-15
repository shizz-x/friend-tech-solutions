import pathlib
from exceptions.exceptions import NotFoundProxyFile, InvalidArgument
import os
import dotenv
class Utility:


    @staticmethod
    def get_proxies() -> list[str]:
        path_to_proxies = pathlib.Path('../file')


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
    
    @staticmethod
    def read_environ(args: list[str]):
        if __name__ == '__main__':
            pathlib.Path('.env').touch()

            if len(args) > 1:
                args.remove('main.py')
                for arg in args:
                    if arg.startswith('--path='):
                        path_to_proxy = arg.replace('--path=', '')
                        if pathlib.Path(path_to_proxy).is_file():
                            os.environ['path_to_proxies'] = path_to_proxy
                            dotenv.set_key(pathlib.Path('.env'), 'path_to_proxies', path_to_proxy)
                        else:
                            raise NotFoundProxyFile(f'path {path_to_proxy} invalid')
            else:
                if not os.environ.get('path_to_proxies'):
                    raise InvalidArgument('missing required argument --path=')