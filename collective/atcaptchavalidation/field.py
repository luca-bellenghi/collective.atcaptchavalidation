from Products.Archetypes import Field
from AccessControl import ClassSecurityInfo
from collective.atcaptchavalidation.widget import CaptchaWidget
from Products.Archetypes.Registry import registerField


class CaptchaField(Field.ObjectField):
    """A field that stores strings"""
    _properties = Field._properties.copy()
    _properties.update({
        'type': 'captcha',
        'required': True,
        'widget': CaptchaWidget,
    })

    security = ClassSecurityInfo()

    security.declarePrivate('get')

    def get(self, instance, **kwargs):
        pass

    security.declarePrivate('set')

    def set(self, instance, value, **kwargs):
        pass

registerField(CaptchaField,
              title='Captcha',
              description='Used for form edit validation')
