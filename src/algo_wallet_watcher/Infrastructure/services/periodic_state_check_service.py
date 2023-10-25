from algo_wallet_watcher.api.services.aww_service import list_wallet
from algo_wallet_watcher.api.endpoints.aww_app import session
from algo_wallet_watcher.Infrastructure.adapters.wallet_repository import WalletRepository


class PeriodicStateCheckService:
    global session
    
    def __init__(self):
        self.wallet_list = list_wallet(WalletRepository(session=session))
        
        
k = PeriodicStateCheckService()

print(k.wallet_list)