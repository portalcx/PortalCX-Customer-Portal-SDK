#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Name: utils/logger.py

Description:

Logger for PortalCX SDK.
"""

import logging

def get_logger() -> logging.Logger:
    """
    Returns a configured logger instance.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Define console handler and formatter
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    return logger
