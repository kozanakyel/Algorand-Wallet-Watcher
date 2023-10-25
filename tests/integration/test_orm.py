from sqlalchemy import text
from algo_wallet_watcher.core.domain.wallet import Wallet


def test_saving_wallets(session):
    wlt = Wallet(
        "SLGYSO6ZRYW5FOJCYPLXSBMKFAGOV3QUZ3AZZ3LRAJMSJDDH63RIJDYJUU", 230543, "Offline"
    )
    session.add(wlt)
    session.commit()
    rows = session.execute(text('SELECT address, amount, state FROM "wallets"'))
    assert list(rows) == [
        (
            "SLGYSO6ZRYW5FOJCYPLXSBMKFAGOV3QUZ3AZZ3LRAJMSJDDH63RIJDYJUU",
            230543,
            "Offline",
        )
    ]


def test_wallet_mapper_can_load(session):
    session.execute(
        text(
            "INSERT INTO wallets (address, amount, state) VALUES "
            '("SLGYSO6ZRYW5FOJCYPLXSBMKFAGOV3QUZ3AZZ3LRAJMSJDDH63RIJDYJUU", 500, "Online"),'
            '("ABCDEFGH123456789012345678901234567890123456789012345678901234567890123456789", 1000, "Offline"),'
            '("XYZABC123456789012345678901234567890123456789012345678901234567890123456789", 200, "Online")'
        )
    )
    expected = [
        Wallet(
            "SLGYSO6ZRYW5FOJCYPLXSBMKFAGOV3QUZ3AZZ3LRAJMSJDDH63RIJDYJUU", 500, "Online"
        ),
        Wallet(
            "ABCDEFGH123456789012345678901234567890123456789012345678901234567890123456789",
            1000,
            "Offline",
        ),
        Wallet(
            "XYZABC123456789012345678901234567890123456789012345678901234567890123456789",
            200,
            "Online",
        ),
    ]
    assert session.query(Wallet).all() == expected


def test_wallet_mapper_can_save(session):
    new_wallet = Wallet(
        "NEWWALLET123456789012345678901234567890123456789012345678901234567890123456789",
        300,
        "Offline",
    )
    session.add(new_wallet)
    session.commit()

    rows = list(session.execute(text('SELECT address, amount, state FROM "wallets"')))
    assert rows == [
        (
            "NEWWALLET123456789012345678901234567890123456789012345678901234567890123456789",
            300,
            "Offline",
        )
    ]


def test_wallet_mapper_can_update(session):
    existing_wallet = Wallet(
        "SLGYSO6ZRYW5FOJCYPLXSBMKFAGOV3QUZ3AZZ3LRAJMSJDDH63RIJDYJUU", 500, "Online"
    )
    session.add(existing_wallet)
    session.commit()

    # Update the state of the wallet
    existing_wallet.state = "Offline"
    session.commit()

    updated_wallet = (
        session.query(Wallet).filter_by(address=existing_wallet.address).first()
    )
    assert updated_wallet.state == "Offline"


def test_wallet_mapper_can_delete(session):
    wallet_to_delete = Wallet(
        "TOBEDELETED123456789012345678901234567890123456789012345678901234567890123456789",
        100,
        "Active",
    )
    session.add(wallet_to_delete)
    session.commit()

    # Delete the wallet
    session.delete(wallet_to_delete)
    session.commit()

    deleted_wallet = (
        session.query(Wallet).filter_by(address=wallet_to_delete.address).first()
    )
    assert deleted_wallet is None
