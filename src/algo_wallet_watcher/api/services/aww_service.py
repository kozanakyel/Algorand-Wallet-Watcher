from __future__ import annotations

from algo_wallet_watcher.core.domain.wallet import Wallet
from algo_wallet_watcher.core.exceptions.invalid_address import InvalidAddress
from algo_wallet_watcher.Infrastructure.adapters.wallet_repository import WalletRepository
from algo_wallet_watcher.core.domain.abstract_base_repository import AbstractBaseRepository

def add_wallet(
    address: str,
    amount: int,
    state: str,
    repo: AbstractBaseRepository,
    session,
) -> None:
    wallet_list = repo.list()
    wallet_address_list = [x.address for x in wallet_list]
    
    if address in wallet_address_list:
        raise InvalidAddress(f"Error This Wallet Address is exist: {wallet}")
    repo.add(Wallet(address, amount, state))
    session.commit()



