from collective.atcaptchavalidation.field import CaptchaField
from collective.atcaptchavalidation.widget import CaptchaWidget
from archetypes.schemaextender.interfaces import ISchemaExtender
from zope.component import adapts
from Products.Archetypes.interfaces.base import IBaseObject
from zope.interfaces import implements
from archetypes.schemaextender.field import ExtensionField


class ExtCaptchaField(ExtensionField, CaptchaField):
    """ A captcha field """


class CaptchaSchemaExtender(object):
    adapts(IBaseObject)
    implements(ISchemaExtender)

    _fields = [
        ExtCaptchaField('captcha',
                        widget=CaptchaWidget(
                            label="Captcha",
                            description="Fill the field to validate the form"
                        )
                        )
    ]

    def __init__(self, context):
        self.context = context

    def getField(self):
        return self._fields
