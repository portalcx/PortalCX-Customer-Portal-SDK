#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Name: CreateCustomerPortal/logger.py

Description:

Logger for CreateCustomerPortal.
"""

import logging


def get_logger() -> logging.Logger:
    """
    Returns a configured logger instance.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Define console handler and formatter
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    return logger