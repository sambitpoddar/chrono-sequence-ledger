# Author: Sambit Poddar
# License: Apache License 2.0
# main.py

import sys
import signal
import time
from network.node import CSLNode
from utils.logger import Logger
from utils.config import Config

def handle_shutdown(signal, frame):
    """
    Handle shutdown by stopping the node and logging the event.
    """
    logger.log("Shutting down CSL node...")
    node.stop()
    logger.log("CSL node stopped.")
    sys.exit(0)

def main():
    # Initialize logger
    global logger
    logger = Logger()

    # Load configuration
    config = Config()

    # Initialize CSL node
    global node
    node = CSLNode(config)

    # Start the node
    try:
        node.start()
    except Exception as e:
        logger.error(f"Error occurred while starting CSL node: {e}")
        handle_shutdown(signal.SIGINT, None)

if __name__ == "__main__":
    # Register signal handler for graceful shutdown
    signal.signal(signal.SIGINT, handle_shutdown)
    signal.signal(signal.SIGTERM, handle_shutdown)

    # Start the main function
    main()

