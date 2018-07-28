# -*- coding: utf-8 -*-
# Copyright 2018 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from requests import get, post, delete
from connection import ENVIRONMENT_BASE_URL, VERSION_API

ENDPOINT = ENVIRONMENT_BASE_URL + VERSION_API + \
    '/shipments/{account}/{reference}'


class Shipment:

    def retrieve(self, account, reference='', **kwargs):
        response = get(
            ENDPOINT.format(account=account, reference=reference),
            params=kwargs,
            headers=self.headers,
        )
        return response

    def book(self, account, action, data):
        response = post(
            ENDPOINT.format(account=account, reference=action),
            json=data,
            headers=self.headers,
        )
        return response

    def delete(self, account, reference=''):
        response = delete(
            ENDPOINT.format(account=account, reference=reference),
            headers=self.headers,
        )
        return response

    def manifest(self, account, **kwargs):
        response = get(
            ENDPOINT.format(account=account),
            params=kwargs,
            headers=self.headers,
        )
        return response
