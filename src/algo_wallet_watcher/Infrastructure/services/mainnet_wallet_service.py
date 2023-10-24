from algo_wallet_watcher.Infrastructure.config import MAINNET_ACCOUNT_API
import requests


class MainnetWalletService:
    """
    Singleton Mainnet WAllet Service for ALGORAND testnet
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MainnetWalletService, cls).__new__(cls)
            cls._instance.main_uri = MAINNET_ACCOUNT_API
        return cls._instance

    def get_account_info(self, algorand_address):
        url = f'{self.main_uri}{algorand_address}'
        headers = {
            'accept': 'application/json'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()  
        else:
            return {'error': f'{response.status_code} - {response.text}'}
    
    
if __name__ == "__main__":
    k = MainnetWalletService()
    print(k.get_account_info('jvadsfkfbasl'))
