from allauth.account.adapter import DefaultAccountAdapter
from django.utils.translation import ugettext_lazy as _

from django import forms


class CusDefaultAccountAdapter(DefaultAccountAdapter):

    def clean_password(self, password, user=None):
        """
        Validates a password. You can hook into this if you want to
        estric the allowed password choices.
        """
        if len(password) >= 6:
            return password
        else:
            raise forms.ValidationError('Password too short.')
