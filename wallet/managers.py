from django.db import models, transaction

from . import exceptions

class TransferManager(models.Manager):
    """Manages the transfer of money from one account to another.

    Arguments:
        models {[type]} -- [description]
    """

    def create(
        self,
        source,
        destination,
        amount,
        user=None,
        reference=None,
        message=None,
    ):
        # Write out transfer (which involves multiple writes).  We use a
        # database transaction to ensure that all get written out correctly.
        self.verify_transfer(
            source,
            destination,
            amount,
            message,
            user
        )
        with transaction.atomic():
            transfer = self.get_queryset().create(
                source=source,
                destination=destination,
                amount=amount,
                authorised_by=user,
                reference=reference,
                message=message,
            )
            # Create transaction records for audit trail
            transfer.entries.create(
                account=source,
                amount=-amount,
                description=message,
            )
            destination_entry = transfer.entries.create(
                account=destination,
                amount=amount,
                description=message,
            )

            # Update the cached balances on the accounts
            source.save()
            destination.save()
            return transfer

    LOCAL_TO_EXTERNAL_ACCOUNT_MAPPING = {}

    def verify_transfer(
        self,
        source,
        destination,
        amount,
        message,
        user=None,
    ):
        """
        Test whether the proposed transaction is permitted.  Raise an exception
        if not.
        Validations for money being withdrawn. These need automated tests
         1) You cannot withdraw from an account in wallet that is not yours as a merchant.
         2) Cash account should have a balance enough to cover transaction fees in a transfer
         3) Te deposit money to a merchant's wallet(revenue) the order line must have been paid for.
         4)

        """
        if amount < 0:
            raise exceptions.InvalidAmount("Debits must use a positive amount")
        if not source.is_open():
            raise exceptions.ClosedAccount("Source account has been closed")
        if user and not source.can_be_authorised_by(user):
            raise exceptions.AccountException(
                "This user is not authorised to make transfers from " "this account"
            )
        if not destination.is_open():
            raise exceptions.ClosedAccount("Destination account has been closed")
        if not source.is_debit_permitted(amount):
            msg = "Unable to debit %.2f from account #%d:"
            raise exceptions.InsufficientFunds(msg % (amount, source.id))