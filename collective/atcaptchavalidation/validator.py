from Products.Archetypes.interfaces import IObjectPreValidation
from zope.component import adapts
from zope.interface import Interface, implements


class CaptchaValidation(object):
    implements(IObjectPreValidation)
    adapts(Interface)

    def __init__(self, context):
        super(CaptchaValidation, self).__init__()
        self.context = context

    def __call__(self, request):
        return None
