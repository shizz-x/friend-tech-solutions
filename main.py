import asyncio

from modules.parser import Parser


async def main():
    parser = Parser()
    print(await parser.get_online_users())


if __name__ == '__main__':
    asyncio.run(main())
