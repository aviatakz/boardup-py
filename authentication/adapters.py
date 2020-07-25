from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.core.exceptions import PermissionDenied


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        u = sociallogin.user
        if not u.email.split('@')[1] == "aviata.me" or u.email.split('@')[1] == "chocotravel.com":
            raise PermissionDenied()