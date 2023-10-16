import pathlib
import os
import dotenv

class Utility:


    @staticmethod
    def get_proxies() -> list[str] | None:
        proxies = [proxy for proxy in open(os.environ['path_to_proxy'], 'r').read().split('\n') if proxy != '']
        if len(proxies) == 0:
            return None
        prepared_proxies = []
        for proxy in proxies:
            prepared_proxies.append(Utility.prepare_proxy(proxy))
        return prepared_proxies
    
    @staticmethod
    def get_keys() -> list[str] | list:
        private_keys = [key for key in open(os.environ['path_to_keys'], 'r').read().split('\n') if key != '']
        if len(private_keys) == 0:
            return []
        return private_keys
    

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
            return f'http://{PROXY_HOST}'

        return f'http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}'
    
    @staticmethod
    def read_environ():

        if not pathlib.Path('.env').is_file():

            pathlib.Path('.env').touch()

            base_http_uri = input('BASE HTTP PROVIDER: ')
            print('Change it in .env')
            os.environ['base_http_uri'] = base_http_uri

            dotenv.set_key(pathlib.Path('.env'), 'base_http_uri', base_http_uri)
        
        if not pathlib.Path('./proxy.txt').is_file():
            
            pathlib.Path('./proxy.txt').touch()
            print("File proxy.txt created, format 'host:port:user:password' or 'host:port'")
        
        if not pathlib.Path('./keys.txt').is_file():
            
            pathlib.Path('./keys.txt').touch()

            input('private keys file created, put some keys newline separated')
            raise ValueError('private keys file created, put some keys newline separated')
        os.environ['path_to_keys'] = str(pathlib.Path('./keys.txt').absolute())
        os.environ['path_to_proxy'] = str(pathlib.Path('./proxy.txt').absolute())
        print(os.environ['path_to_keys'])

        
        




            