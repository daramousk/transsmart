# -*- coding: utf-8 -*-
# Copyright 2018 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from requests import post
from connection import ENVIRONMENT_BASE_URL, VERSION_API

ENDPOINT = ENVIRONMENT_BASE_URL + VERSION_API + '/rates/{account}'


class Rate:

    def calculate(self, account, data):
        response = post(ENDPOINT.format(account=account),
            json=data,
            headers=self.headers)
        return response
