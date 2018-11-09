# -*- coding: utf-8 -*-
# Copyright 2018 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from requests import post


class Rate:

    endpoint = '/rates/{account}'

    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def calculate(self, account, data):
        response = post(
            self.base_url + self.endpoint.format(account=account),
            json=data,
            headers=self.headers)
        return response
