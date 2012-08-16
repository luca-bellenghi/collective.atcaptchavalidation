# -*- coding: utf-8 -*-

from collective.atcaptchavalidation.tests.base import TestCase
from zope.component import getUtility, provideAdapter
from plone.registry.interfaces import IRegistry
from collective.atcaptchavalidation.controlpanel import ICaptchaSettingsControlPanel
from collective.atcaptchavalidation.extender import CaptchaSchemaExtender


class TestATCaptchaValidation(TestCase):

    def afterSetUp(self):
        self.setRoles(('Contributor', ))
        registry = getUtility(IRegistry)
        self.settings = registry.forInterface(ICaptchaSettingsControlPanel)
        provideAdapter(CaptchaSchemaExtender,
                        name='collective.atcapthcavalidation.schemaextender')

    def test_registry(self):
        check = hasattr(self.settings, 'captcha_validated_fields')
        self.assertTrue(check)

    def test_type_without_captcha(self):
        self.portal.invokeFactory('Document', id='my_page')
        mypage = self.portal['my_page']
        field = mypage.getField('recaptcha_response_field')
        self.assertEqual(None, field)

    def test_type_with_capthca(self):
        self.settings.captcha_validated_fields = 'Document',
        self.portal.invokeFactory('Document', id='my_page')
        mypage = self.portal['my_page']
        # In test no problem with checkCreationFlag
        fcn = mypage.getField('recaptcha_response_field').__class__.__name__
        self.assertEqual('ExtCaptchaField', fcn)


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestATCaptchaValidation))
    return suite
