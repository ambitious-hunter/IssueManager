# from django.conf import settings
# from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailAuth(object):

    def authenticate(self, email=None, password=None):
        """
       Get an instance of User using the supplied email and check its password
       """
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user

        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
       Used by the django authentication system to retrieve an instance of User
       """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
