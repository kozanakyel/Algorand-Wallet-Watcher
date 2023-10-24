import os
from dotenv import load_dotenv
from datetime import datetime
from algo_wallet_watcher.Infrastructure.logger.logger import Logger

load_dotenv()


LOG_PATH = './src/algo_wallet_watcher/Infrastructure/logger' + os.sep + "logs"
LOG_FILE_NAME_PREFIX = f"log_{datetime.now()}"

API_PORT='5000'
API_HOST='127.0.0.1'

def get_api_url():
    host = API_HOST
    port = API_PORT
    return f"http://{host}:{port}"


def get_db_uri():
    return 'sqlite:///database.db'