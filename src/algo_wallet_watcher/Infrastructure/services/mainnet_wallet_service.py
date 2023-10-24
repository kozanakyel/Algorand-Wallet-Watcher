from algo_wallet_watcher.Infrastructure.config import MAINNET_ACCOUNT_API


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


if __name__ == "__main__":
    k = MainnetWalletService()
    print(k.main_uri)
