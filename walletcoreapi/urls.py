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
    # url(
    #     r"^transfers/$",
    #     wallet.TransfersListView.as_view(),
    #     name="user-transfers",
    # ),
    url(
        r"^users/$",
        accounts.WalletUserListView.as_view(),
        name="wallet-users",
    ),
    url(
        r"^users/(?P<pk>-?\d+)/$",
        accounts.WalletUserDetailView.as_view(),
        name="wallet-user-details",
    ),
    # url(
    #     r"^users/(?P<pk>-?\d+)/profile/$",
    #     accounts.WalletUserProfileView.as_view(),
    #     name="user-profile",
    # ),
    url(
        r"^users/(?P<userid>-?\d+)/transactions/$",
        accounts.WalletUserTransactionView.as_view(),
        name="user-transactions",
    ),
    url(
        r"^users/(?P<pk>-?\d+)/wallet/$",
        wallet.WalletDetailView.as_view(),
        name="user-wallets",
    ),
    url(
        r"^users/(?P<pk>-?\d+)/account/$",
        wallet.AccountDetailView.as_view(),
        name="user-accounts",
    ),
    # url(
    #     r"^profiles/$",
    #     accounts.ProfileListView.as_view(),
    #     name="user-profiles",
    # ),
    url(
        r"^users/(?P<userid>-?\d+)/wallet/transfer/$",
        wallet.WalletTransferView.as_view(),
        name="partner-wallet-transaction",
    ),
    url(
        r"^users/(?P<userid>-?\d+)/wallet/transact/$",
        wallet.AccountDepositWithdrawView.as_view(),
        name="partner-wallet-transaction",
    ),
    url(
        r"^users/(?P<userid>-?\d+)/transactions/$",
        wallet.AccountEntryListView.as_view(),
        name="user-account-transactions",
    ),

]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]