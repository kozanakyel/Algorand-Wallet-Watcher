from algo_wallet_watcher.core.domain.wallet import Wallet
from algo_wallet_watcher.Infrastructure.adapters.wallet_repository import (
    WalletRepository,
)


def test_add_wallet(session):
    repo = WalletRepository(session)
    wallet = Wallet(
        "SLGYSO6ZRYW5FOJCYPLXSBMKFAGOV3QUZ3AZZ3LRAJMSJDDH63RIJDYJUU", 230543, "Offline"
    )
    repo.add(wallet)
    assert repo.get(wallet.address) == wallet


def test_get_wallet(session):
    repo = WalletRepository(session)
    wallet = Wallet(
        "SLGYSO6ZRYW5FOJCYPLXSBMKFAGOV3QUZ3AZZ3LRAJMSJDDH63RIJDYJUU", 230543, "Offline"
    )
    repo.add(wallet)
    retrieved_wallet = repo.get(wallet.address)
    assert retrieved_wallet == wallet
    assert retrieved_wallet.address == wallet.address
    assert retrieved_wallet.amount == wallet.amount
    assert retrieved_wallet.state == wallet.state


def test_list_wallets(session):
    repo = WalletRepository(session)
    wallet1 = Wallet(
        "SLGYSO6ZRYW5FOJCYPLXSBMKFAGOV3QUZ3AZZ3LRAJMSJDDH63RIJDYJUU", 230543, "Offline"
    )
    wallet2 = Wallet(
        "XYZABC123456789012345678901234567890123456789012345678901234567890123456789",
        200,
        "Online",
    )
    repo.add(wallet1)
    repo.add(wallet2)
    wallets = repo.list()
    assert wallet1 in wallets
    assert wallet2 in wallets


def test_update_wallet(session):
    repo = WalletRepository(session)
    wallet = Wallet(
        "SLGYSO6ZRYW5FOJCYPLXSBMKFAGOV3QUZ3AZZ3LRAJMSJDDH63RIJDYJUU", 230543, "Offline"
    )
    repo.add(wallet)

    # Update the wallet
    repo.update(address=wallet.address, amount=300, state="Online")

    updated_wallet = repo.get(wallet.address)
    assert updated_wallet.amount == 300
    assert updated_wallet.state == "Online"
