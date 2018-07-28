# -*- coding: utf-8 -*-
# Copyright 2018 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from requests.auth import HTTPBasicAuth
from requests import get
from connection import ENVIRONMENT_BASE_URL
ENDPOINT = ENVIRONMENT_BASE_URL + '/login'


class Authentication:

    def authenticate(self, username, password):
        response = get(ENDPOINT, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        self.token = 'Bearer ' + response.json()['token']
        self.header = {
            'Authorization': self.token,
            'Content-Type': 'application/json',
        }
        return self.header
