# -*- coding: utf-8 -*-
# Copyright 2018 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from requests import get, post, put, delete
from connection import ENVIRONMENT_BASE_URL, VERSION_API

ENDPOINT = ENVIRONMENT_BASE_URL + VERSION_API + '/addresses/{account}/{_id}'


class Address:

    def retrieve(self, account, _id):
        response = get(
            ENDPOINT.format(account=account, _id=_id),
            headers=self.headers)
        return response

    def create(self, account, params):
        response = post(
            ENDPOINT.format(account=account, _id=''),
            json=params,
            headers=self.headers)
        return response

    def update(self, account, _id, params):
        response = put(
            ENDPOINT.format(account=account, _id=_id),
            json=params,
            headers=self.headers)
        return response

    def delete(self, account, _id):
        response = delete(
            ENDPOINT.format(account=account, _id=_id),
            headers=self.headers)
        return response
