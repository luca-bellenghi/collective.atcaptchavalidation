# -*- coding: utf-8 -*-
from zope.interface import implements
from Products.validation.interfaces import ivalidator
from Products.CMFPlone import PloneMessageFactory as _


class CaptchaValidation(object):
    implements(ivalidator)

    def __init__(self, name):
        self.name = name

    def __call__(self, value, *args, **kwargs):
        request = kwargs['REQUEST']
        instance = kwargs['instance']
        captcha_view = instance.restrictedTraverse('@@captcha', None)
        captcha_control = request.get('captcha_control', None)
        if captcha_view and captcha_control:
            captcha = request.get('recaptcha_response_field', '')
            if not captcha_view.verify(captcha):
                return _(u'wrong_captcha', default=u"The captcha is wrong")
            return None
        else:
            return _(u"captcha_not_verified",
                     default=u"Not possible to verify the captcha")
