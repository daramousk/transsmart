# -*- coding: utf-8 -*-
# Copyright 2018 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from requests import get


class Location:

    endpoint = '/prints/{account}/{reference}'

    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def retrieve(self, account, **kwargs):
        response = get(
            self.base_url + self.endpoint.format(account=account),
            params=kwargs,
            headers=self.headers)
        return response
