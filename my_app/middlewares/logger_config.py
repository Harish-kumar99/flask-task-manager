import logging

# Define color codes
COLOR_CODES = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'reset': '\033[0m'  # Reset color to default
}


# Define log format with colors
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
COLOR_FORMAT = f'{COLOR_CODES["green"]}%(asctime)s{COLOR_CODES["reset"]} - ' \
               f'{COLOR_CODES["blue"]}%(levelname)s{COLOR_CODES["reset"]} - ' \
               f'%(message)s'

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Create console handler with colored formatter
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter(COLOR_FORMAT, datefmt='%Y-%m-%d %H:%M:%S')
    console_handler.setFormatter(console_formatter)

    # Add console handler to the logger
    logger.addHandler(console_handler)

    return logger
