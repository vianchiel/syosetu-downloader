import os
import logging

from assets.noct import noct_downloader

def main():
    # Setup logging
    logging.basicConfig(
        #filename='myapp.log', 
        level=logging.DEBUG
    )
    logging.info("Application started.")
    noct_session = noct_downloader()


if __name__ == '__main__':
    # todo: 
    # Initialise the configurations reader
    # Check args
    # Initiate download queue
    main()