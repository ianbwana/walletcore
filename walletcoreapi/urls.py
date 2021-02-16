from django.urls import path
from django.conf.urls import include, url
from rest_framework_swagger.views import get_swagger_view



from walletcoreapi.views.wallet import (
    TransfersListView,
    WalletListView,
    AccountsListView
)
schema_view = get_swagger_view(title='MobileWallet2020')
urlpatterns = [
    url(r'^docs/', schema_view, name='walletcore-api-docs'),
    url(
        r"^transfers/$",
        TransfersListView.as_view(),
        name="transfers",
    ),
    url(
        r"^wallets/$",
        WalletListView.as_view(),
        name="wallets",
    ),
    url(
        r"^accounts/$",
        AccountsListView.as_view(),
        name="accounts",
    ),
]