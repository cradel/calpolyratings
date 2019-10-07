
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from allauth.account.utils import filter_users_by_username


def username_checker(value):
    #print('username_checker validator started')
    if not (re.fullmatch("[0-9a-zA-Z-_]+", value) and len(value) >= 3 and len(value) <= 20):
        raise ValidationError(
            _('Criteria not met.')
        )
    error_messages = {'username_taken': 'Username is taken.'}


def username_check_if_unique(value):
    #print('username_check_if_unique validator started')
    if filter_users_by_username(value).exists():
        error_message = error_messages['username_taken']
        raise ValidationError(error_message)


def check_calpoly_email(value):
    if value is None:
        raise ValidationError("")

    arr = value.split('@')
    print(arr[1])
    if(len(arr) > 2 or arr[1] != 'calpoly.edu'):
        raise ValidationError("Bad email")


username_validators = [username_check_if_unique, username_checker]
