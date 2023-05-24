#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Name: Setup.py

Description:
This script is used to package the PortalCX Python SDK as a pip package.
"""

from setuptools import setup, find_packages

# Read requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='portalcx',
    version='1.0.0',
    description='Python SDK for PortalCX',
    author='Matthew Schwen',
    author_email='matt@portalcx.com',
    url='https://github.com/portalcx/PortalCX-Customer-Portal-SDK',
    packages=find_packages(),
    install_requires=required,
)