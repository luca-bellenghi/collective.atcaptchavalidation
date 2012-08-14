
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
               description=('Renders a collective.recaptcha widget'),
               used_for=('collective.atcaptchavalidation.Field.CaptchaField',)
               )
