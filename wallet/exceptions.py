class AccountException(Exception):
    pass


class WalletException(Exception):
    pass


class AccountNotEmpty(AccountException):
    pass


class InsufficientFunds(AccountException):
    pass


class InvalidAmount(AccountException):
    pass

class InactiveAccount(AccountException):
    pass

class ClosedAccount(AccountException):
    pass


class NoPaymentException(AccountException):
    pass


class MultipleCashAccounts(AccountException):
    pass


class PermissionException(Exception):
    pass


class TransferException(Exception):
    pass



class DuplicateTransaction(TransferException):
    pass
