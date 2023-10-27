from algo_wallet_watcher.Infrastructure.services.mainnet_wallet_service import (
    MainnetWalletService,
)
from algo_wallet_watcher.api.services.aww_service import list_wallet
from algo_wallet_watcher.api.endpoints.aww_app import session
from algo_wallet_watcher.Infrastructure.adapters.wallet_repository import (
    WalletRepository,
)
from algo_wallet_watcher.core.domain.wallet import Wallet
from algo_wallet_watcher.Infrastructure.logger.logger import Logger
from algo_wallet_watcher.Infrastructure.config import LOG_FILE_NAME_PREFIX, LOG_PATH

import threading
import time
import logging


class PeriodicStateCheckService:
    global session

    def __init__(self):
        self.wallet_repo = WalletRepository(session=session)
        self.wallet_list = list_wallet(self.wallet_repo)
        self.mainnet_service = MainnetWalletService()
        # self.logger = Logger(LOG_PATH, LOG_FILE_NAME_PREFIX)
        self.logger = logging
        self.periodic_thread = threading.Thread(target=self.periodic_state_check)
        self.periodic_thread.daemon = True
        # print("file path logger: ", self.logger.file_path)

    def get_account_info(self, address):
        return self.mainnet_service.get_account_info(address)

    def log(self, text):
        if self.logger:
            self.logger.warning(text)
        else:
            print(text)

    def periodic_state_check(self):
        while True:
            for wallet in self.wallet_list:
                address = wallet.address
                current_state = self.get_account_info(address)
                # print(current_state)

                if "error" not in current_state:
                    if current_state["amount"] != wallet.amount:
                        self.log(
                            f"amount changed for wallet {address}. "
                            f"Old amount: {wallet.amount}, New balance: {current_state['amount']}"
                        )
                        wallet.amount = current_state["amount"]

                    if current_state["state"] != wallet.amount:
                        wallet.state = current_state["state"]

                    self.wallet_repo.update(
                        address=address,
                        amount=current_state["amount"],
                        state=current_state["state"],
                    )

            time.sleep(60)        
        

    def start_periodic_check(self):
        print("Priodic State Check Service start running...")
        self.periodic_thread.start()
