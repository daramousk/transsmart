# -*- coding: utf-8 -*-
# Copyright 2018 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from requests.auth import HTTPBasicAuth
from requests import get


class Authentication():

    endpoint = '/login'

    def __init__(self, base_url):
        self.base_url = base_url

    def authenticate(self, username, password):
        response = get(
            self.base_url + self.endpoint,
            auth=HTTPBasicAuth(username, password)
        )
        response.raise_for_status()
        self.token = 'Bearer ' + response.json()['token']
        self.header = {
            'Authorization': self.token,
            'Content-Type': 'application/json',
        }
        return self.header
