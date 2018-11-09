# -*- coding: utf-8 -*-
# Copyright 2018 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from requests import get, post, delete


class Shipment:

    endpoint = '/shipments/{account}/{reference}'

    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def retrieve(self, account, reference='', **kwargs):
        response = get(
            self.base_url + self.endpoint.format(
                account=account,
                reference=reference),
            params=kwargs,
            headers=self.headers,
        )
        return response

    def book(self, account, action, data):
        response = post(
            self.base_url + self.endpoint.format(
                account=account, reference=action),
            json=data,
            headers=self.headers,
        )
        return response

    def delete(self, account, reference=''):
        response = delete(
            self.base_url + self.endpoint.format(
                account=account, reference=reference),
            headers=self.headers,
        )
        return response

    def manifest(self, account, **kwargs):
        response = get(
            self.base_url + self.endpoint.format(account=account),
            params=kwargs,
            headers=self.headers,
        )
        return response
