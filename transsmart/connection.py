# -*- coding: utf-8 -*-
# Copyright 2018 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from importlib import import_module
ENVIRONMENT_BASE_URL = 'https://accept-api.transsmart.com'
# TODO change to prod
VERSION_API = '/v2'

import authentication

class Connection:

    headers = None

    def connect(self, username, password):
        self.headers =  authentication.Authentication().authenticate(username, password)
        return self

    def __getattr__(self, name):
        mod = import_module('.{}'.format(name.lower()), 'transsmart')
        attr =  getattr(mod, name)()
        attr.headers = self.headers
        return attr

    def __repr__(self):
        return 'Connection {}'.format(True if self.headers else False)
