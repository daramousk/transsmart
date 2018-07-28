# -*- coding: utf-8 -*-
# Copyright 2018 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from setuptools import setup, find_packages

setup(
    name="Transsmart V2",
    version="0.1",
    packages=find_packages(),
    scripts=['bin/transsmart'],
    install_requires=['requests'],
)
