from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed


class EmailJWTAuthentication(JWTAuthentication):
    pass
    # def get_user(self, validated_token):
    #     """
    #     Attempts to find and return a user using the given validated token.
    #     """
    #     User = get_user_model()
    #     try:
    #         email = validated_token['email']
    #     except KeyError:
    #         raise InvalidToken(_("Token contained no recognizable email"))
    #
    #     try:
    #         user = User.objects.get(email=email)
    #     except User.DoesNotExist:
    #         raise AuthenticationFailed(_("User not found"), code="user_not_found")
    #
    #     if not user.is_active:
    #         raise AuthenticationFailed(_("User is inactive"), code="user_inactive")
    #
    #     return user
