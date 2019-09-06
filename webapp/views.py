from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.models import JSONField
from users.models import CustomUser

from django.db import connection
# print(connection.queries[-1])

def home(request):

    # user = request.user
    # socialuser = SocialAccount.objects.filter(user=user, provider='github')[0]
    # print(socialuser)

    # for item in SocialAccount.objects.all():
    #     print(item.extra_data)

    # context = {"extra_data": SocialAccount.objects.values('extra_data')}

    return render(request, 'home.html')
