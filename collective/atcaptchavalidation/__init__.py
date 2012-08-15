# -*- coding: utf-8 -*-

from zope.i18nmessageid import MessageFactory
import logging

captchavalidationMessageFactory = MessageFactory('collective.atcaptchavalidation')
logger = logging.getLogger('collective.atcaptchavalidation')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
