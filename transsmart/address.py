# -*- coding: utf-8 -*-
# Copyright 2018 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from requests import get, post, put, delete


class Address:

    endpoint = '/addresses/{account}/{_id}'

    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def retrieve(self, account, _id):
        response = get(
            self.base_url + self.endpoint.format(account=account, _id=_id),
            headers=self.headers)
        return response

    def create(self, account, params):
        response = post(
            self.base_url + self.endpoint.format(account=account, _id=''),
            json=params,
            headers=self.headers)
        return response

    def update(self, account, _id, params):
        response = put(
            self.base_url + self.endpoint.format(account=account, _id=_id),
            json=params,
            headers=self.headers)
        return response

    def delete(self, account, _id):
        response = delete(
            self.base_url + self.endpoint.format(account=account, _id=_id),
            headers=self.headers)
        return response
