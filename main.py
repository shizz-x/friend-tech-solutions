import sys
import os
import pathlib
import dotenv 
from exceptions import exceptions

from modules.utils import Utility as utils

dotenv.load_dotenv()



def main(args: list[str] = sys.argv):
    utils.read_environ(args)
    



if __name__ == '__main__':
    main()
