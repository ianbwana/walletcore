from django.db.models import Count, Min, Sum
from datetime import datetime

from . import exceptions
from wallet.models import AccountEntry


def get_account_balance(account_id):
    debits = AccountEntry.objects.filter(
        account__id=account_id,
        transaction__transaction_type="debit"
    ).values('amount').aggregate(
        Sum('amount')
    )
    credits = AccountEntry.objects.filter(
        account__id=account_id,
        transaction__transaction_type="credit"
    ).values('amount').aggregate(
        Sum('amount')
    )
    if credits['amount__sum'] is None:
        credits['amount__sum'] = 0
    elif debits['amount__sum'] is None:
        debits['amount__sum'] = 0

    if credits['amount__sum'] is not None and debits['amount__sum'] is not None:
        balance = int(credits['amount__sum']) + int(debits['amount__sum'])
    else:
        balance = 0

    return balance
