# -*- coding: utf-8 -*-
# Copyright 2018 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from requests import get
from connection import ENVIRONMENT_BASE_URL, VERSION_API

ENDPOINT = ENVIRONMENT_BASE_URL + VERSION_API + \
    '/statuses/{account}/shipments/{reference}'


class Status:

    def retrieve(self, account, reference='', **kwargs):
        response = get(
            ENDPOINT.format(account=account, reference=reference),
            params=kwargs,
            headers=self.headers)
        return response
