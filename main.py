import dotenv 
from modules.utils import Utility as utils
utils.read_environ()
dotenv.load_dotenv()
from modules.core import Core





def main():
    core = Core()

    core.start_procces()

if __name__ == '__main__':
    main()
