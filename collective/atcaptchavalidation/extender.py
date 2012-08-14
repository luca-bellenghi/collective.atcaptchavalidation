
from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField

from plone.registry.interfaces import IRegistry

from zope.component import adapts, getUtility
from zope.interface import implements

from Products.Archetypes.interfaces.base import IBaseObject
from Products.validation import validation

from collective.atcaptchavalidation.controlpanel import ICaptchaSettingsControlPanel
from collective.atcaptchavalidation.field import CaptchaField, CaptchaWidget
from collective.atcaptchavalidation.validator import CaptchaValidation

validation.register(CaptchaValidation('isValidCaptcha'))


class ExtCaptchaField(ExtensionField, CaptchaField):
    """ A captcha field """


class CaptchaSchemaExtender(object):
    adapts(IBaseObject)
    implements(ISchemaExtender)

    _fields = [
        ExtCaptchaField('recaptcha_response_field',
                        validators=('isValidCaptcha', ),
                        widget=CaptchaWidget(
                            label="Captcha",
                            description="Fill the field to validate the form"
                        )
                        )
    ]

    def __init__(self, context):
        self.context = context

    def get_captcha_types(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ICaptchaSettingsControlPanel)
        return settings.captcha_validated_fields or tuple()

    def getFields(self):
        """
        The context should provide IBaseObject
        The creation flag shoul be True
        The context portal_type should be in the list of types with captcha validation
        """
        first_cond = IBaseObject.providedBy(self.context)
        second_cond = self.context.checkCreationFlag()
        third_cond = self.context.portal_type in self.get_captcha_types()
        if first_cond and second_cond and third_cond:
            return self._fields
        return []
