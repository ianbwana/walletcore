from django.urls import path
from django.conf.urls import include, url
from rest_framework_swagger.views import get_swagger_view



from walletcoreapi.views import(
    wallet,
    accounts
)
schema_view = get_swagger_view(title='MobileWallet2020')
urlpatterns = [
    url(r'^docs/', schema_view, name='walletcore-api-docs'),
    url(
        r"^transfers/$",
        wallet.TransfersListView.as_view(),
        name="user-transfers",
    ),
    url(
        r"^wallets/$",
        wallet.WalletListView.as_view(),
        name="user-wallets",
    ),
    url(
        r"^accounts/$",
        wallet.AccountsListView.as_view(),
        name="user-accounts",
    ),
    url(
        r"^profiles/$",
        accounts.ProfileListView.as_view(),
        name="user-profiles",
    ),

]