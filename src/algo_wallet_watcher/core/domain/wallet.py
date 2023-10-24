class Wallet:
    """
    Represents a Algorand Wallet with its address, amount/balance, and State.

    This class provides a way to store and retrieve information about a Algo wallet.

    Attributes:
        address (str): The address of the wallet.
        amount (int): The balance of wallet.
        state (str): State of this wallet.

    Methods:
        json(): Returns the wallet as a JSON-compatible dictionary.
    """

    def __init__(self, address: str, amount: int, state: str):
        self.address = address
        self.amount = amount
        self.state = state

    def __eq__(self, other):
        """
        Compare if two wallet are equal.

        Parameters:
            other (Wallet): The other addres of wallet.

        Returns:
            bool: True if the wallets are equal, False otherwise.
        """
        if not isinstance(other, Wallet):
            return False
        return other.address == self.address

    def json(self):
        """
        Return the wallet as a JSON-compatible dictionary.

        Returns:
            dict: A dictionary representing the wallet.
        """
        return {
            'address': self.address,
            'amount': self.amount,
            'state': self.state
        }

    def __repr__(self):
        """
        Return a string representation of the wallet.

        Returns:
            str: A string representation of the wallet.
        """
        return f"<Wallet {self.address}>"