from logger import logger
from app import MainApp


def main():
    app = MainApp()
    app.run()
    
    
    
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception(e)