# -*- coding: utf-8 -*-

from account.accounts import Account
from account.decorators import login_exempt


@login_exempt
def logout(request):
    account = Account()
    return account.logout(request)
