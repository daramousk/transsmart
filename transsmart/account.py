# -*- coding: utf-8 -*-
# Copyright 2018 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from requests import get
from connection import ENVIRONMENT_BASE_URL, VERSION_API

ENDPOINT = ENVIRONMENT_BASE_URL + VERSION_API + \
    '/accounts/{account}/listsettings/{_type}/{nr}'


class Account:

    def retrieve_carrier(self, account, nr=''):
        response = get(
            ENDPOINT.format(account=account, nr=nr, _type='carriers'),
            headers=self.headers)
        return response

    def retrieve_costcenter(self, account, nr=''):
        response = get(
            ENDPOINT.format(account=account, nr=nr, _type='costCenters'),
            headers=self.headers)
        return response

    def retrieve_incoterms(self, account, nr=''):
        response = get(
            ENDPOINT.format(account=account, nr=nr, _type='incoterms'),
            headers=self.headers)
        return response

    def retrieve_mailtypes(self, account, nr=''):
        response = get(
            ENDPOINT.format(account=account, nr=nr, _type='mailTypes'),
            headers=self.headers)
        return response

    def retrieve_packages(self, account, nr=''):
        response = get(
            ENDPOINT.format(account=account, nr=nr, _type='packages'),
            headers=self.headers)
        return response

    def retrieve_servicelevel_time(self, account, nr=''):
        response = get(
            ENDPOINT.format(account=account, nr=nr, _type='serviceLevelTimes'),
            headers=self.headers)
        return response

    def retrieve_servicelevel_others(self, account, nr=''):
        response = get(
            ENDPOINT.format(
                account=account, nr=nr, _type='serviceLevelOthers'),
            headers=self.headers)
        return response

    def retrieve_bookingprofiles(self, account, nr=''):
        response = get(
            ENDPOINT.format(account=account, nr=nr, _type='bookingProfiles'),
            headers=self.headers)
        return response
