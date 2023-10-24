from sqlalchemy import Table, MetaData, Column, Integer, String
from sqlalchemy.orm import registry

from algo_wallet_watcher.core.domain.wallet import Wallet

mapper_registry = registry()

metadata = MetaData()

wallets = Table(
    "wallets",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("address", String(58), unique=True),
    Column("amount", Integer),
    Column("state", String(40))
)

def start_mappers():
    mapper_registry.map_imperatively(Wallet, wallets)

