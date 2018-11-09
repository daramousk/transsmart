# -*- coding: utf-8 -*-
# Copyright 2018 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from importlib import import_module
URL_PRODUCTION = 'https://api.transsmart.com/v2'
URL_USER_ACCEPTANCE = 'https://accept-api.transsmart.com/v2'


class Connection:

    base_url = None
    headers = None

    def connect(self, username, password, acceptance):
        if acceptance:
            self.base_url = URL_USER_ACCEPTANCE
        else:
            self.base_url = URL_PRODUCTION
        from . import authentication
        auth_url = self.base_url.replace('/v2', '')
        self.headers = authentication.Authentication(
                auth_url).authenticate(username, password)
        return self

    def __getattr__(self, name):
        mod = import_module('.{}'.format(name.lower()), 'transsmart')
        attr =  getattr(mod, name)(self.base_url, self.headers)
        attr.headers = self.headers
        return attr

    def __repr__(self):
        return 'Connected {}'.format(self.connected)
