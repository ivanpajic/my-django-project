from __future__ import unicode_literals

from django.apps import AppConfig

from retry.api import retry_call


class CartConfig(AppConfig):

    name = 'cart'

def foo() -> None:
    retry_call(f=bar, tries=3)


def bar() -> None:
    pass
