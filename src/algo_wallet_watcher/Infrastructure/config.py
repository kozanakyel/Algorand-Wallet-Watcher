import os
from dotenv import load_dotenv
from datetime import datetime
from algo_wallet_watcher.Infrastructure.logger.logger import Logger

load_dotenv()

MAINNET_ACCOUNT_API = 'https://mainnet-api.algonode.cloud/v2/accounts/'

LOG_PATH = './src/algo_wallet_watcher/Infrastructure/logger' + os.sep + "logs"
LOG_FILE_NAME_PREFIX = f"log_{datetime.now()}"

API_PORT='5005'
API_HOST='127.0.0.1'

SWAGGER_URL = "/swagger"
SWAGGER_API_URL = f"{API_HOST}:{API_PORT}/swagger.json"
SWAGGER_JSON_URL = "src/algo_wallet_watcher/api/endpoints/static/swagger.json"

def get_api_url():
    host = API_HOST
    port = API_PORT
    return f"http://{host}:{port}"


def get_db_uri():
    return 'sqlite:///database.db'