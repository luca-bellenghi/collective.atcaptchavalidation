# -*- coding: utf-8 -*-
from Products.Archetypes import Field
from AccessControl import ClassSecurityInfo
from Products.Archetypes.Registry import registerField
from Products.Archetypes.Widget import TypesWidget
from Globals import InitializeClass
from Products.Archetypes.Registry import registerWidget


class CaptchaWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'modes': ('edit'),
        'visible': {'edit': 'visible', 'view': 'invisible'},
        'macro': 'captchawidget',
    })

InitializeClass(CaptchaWidget)

registerWidget(CaptchaWidget,
               title='CaptchaWidget',
               description=u'Renders a collective.recaptcha widget',
               used_for=('collective.atcaptchavalidation.Field.CaptchaField',)
               )


class CaptchaField(Field.ObjectField):
    """A field that stores strings"""
    _properties = Field.ObjectField._properties.copy()
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
