from __future__ import annotations
from algo_wallet_watcher.Infrastructure.services.mainnet_wallet_service import (
    MainnetWalletService,
)

from algo_wallet_watcher.core.domain.wallet import Wallet
from algo_wallet_watcher.core.exceptions import exceptions
from algo_wallet_watcher.core.domain.abstract_base_repository import (
    AbstractBaseRepository,
)


def add_wallet(
    address: str,
    repo: AbstractBaseRepository,
    session,
) -> None:
    # Check address length is 58 or not
    address = address.strip()
    if len(address) != 58:
        raise exceptions.InvalidAddressLength(
            f"Error This Wallet Address has not length 58"
        )

    # Check wallet is already registered or not
    wallet_list = repo.list()
    wallet_address_list = [x.address for x in wallet_list]
    if address in wallet_address_list:
        raise exceptions.RegisteredAddress(
            f"Error This Wallet Address is Registered: {address}"
        )

    # Check the address is absolutely Algorand Wallet
    mainnet_api = MainnetWalletService()
    response_mainnet = mainnet_api.get_account_info(algorand_address=address)
    if "error" in response_mainnet:
        raise exceptions.InvalidAddress("This is not Algorand Wallet Address!")

    repo.add(
        Wallet(
            address=response_mainnet["address"],
            amount=response_mainnet["amount"],
            state=response_mainnet["state"],
        )
    )
    session.commit()


def list_wallet(repo: AbstractBaseRepository):
    wallet_list = repo.list()
    return wallet_list
