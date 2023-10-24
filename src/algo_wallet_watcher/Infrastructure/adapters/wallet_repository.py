import abc
from algo_wallet_watcher.core.domain.abstract_base_repository import AbstractBaseRepository
from algo_wallet_watcher.core.domain.wallet import Wallet


class AbstractWalletRepository(AbstractBaseRepository):
    @abc.abstractmethod
    def add(self, wallet: Wallet):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, address) -> Wallet:
        raise NotImplementedError

    @abc.abstractmethod
    def list(self):
        raise NotImplementedError


class WalletRepository(AbstractWalletRepository):
    def __init__(self, session):
        self.session = session

    def add(self, wallet):
        self.session.add(wallet)

    def get(self, address):
        return self.session.query(Wallet).filter_by(address=address).first()

    def list(self):
        return self.session.query(Wallet).all()