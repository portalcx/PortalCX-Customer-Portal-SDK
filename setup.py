#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Name: Setup.py

Description:
This script is used to package the shared code as a pip package.
"""

from setuptools import setup

setup(
    name='portalcx_shared_code',
    version='1.0.0',
    description='Shared code for Function Apps',
    author='Matthew Schwen',
    author_email='matt@portalcx.io',
    url='https://github.com/portalcx/PortalCX-Customer-Portal-SDK',
    packages=['utils', 'api'],
    install_requires=[
        'requests',
        'httpx',
        'python-dotenv'
    ],
)
