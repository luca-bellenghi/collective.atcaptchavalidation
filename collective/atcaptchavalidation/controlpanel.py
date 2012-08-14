from zope.interface import Interface, implements
from zope import schema
from zope.component import adapts
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from plone.app.controlpanel.form import ControlPanelForm
from zope.formlib import form
from plone.protect import CheckAuthenticator
from Products.statusmessages.interfaces import IStatusMessage
from zope.component import getMultiAdapter
from zope.component import getUtility
from plone.registry.interfaces import IRegistry


class ICaptchaSettingsControlPanel(Interface):

    captcha_validated_fields = schema.Tuple(
        title=u"Portal types that may use captcha validation",
        description=u"Select portal types that should be captcha validated",
        missing_value=tuple(),
        value_type=schema.Choice(vocabulary="plone.app.vocabularies.UserFriendlyTypes"),
        required=False
    )


class CaptchaSettingsControlPanel(ControlPanelForm):

    implements(ICaptchaSettingsControlPanel)
    form_fields = form.FormFields(ICaptchaSettingsControlPanel)
    label = u'AT settings for captcha field'
    description = u'Select here which kind of object should be capthca validated'
    form_name = u'AT Captcha validation settings'

    @form.action(u'Save', name=u'save')
    def handle_edit_action(self, action, data):
        CheckAuthenticator(self.request)
        if form.applyChanges(self.context, self.form_fields, data,
                             self.adapters):
            self.status = u"Changes saved."
            self._on_save(data)
        else:
            self.status = "No changes made."

    @form.action('Cancel', name=u'cancel')
    def handle_cancel_action(self, action, data):
        IStatusMessage(self.request).addStatusMessage("Changes canceled.", type="info")
        url = getMultiAdapter((self.context, self.request), name='absolute_url')()
        self.request.response.redirect(url + '/plone_control_panel')
        return ''


class CaptchaSettingsControlPanelAdapter(SchemaAdapterBase):
    adapts(IPloneSiteRoot)
    implements(ICaptchaSettingsControlPanel)

    def __init__(self, context):
        super(CaptchaSettingsControlPanelAdapter, self).__init__(context)
        self.context = context

    def get_captcha_validated_fields(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ICaptchaSettingsControlPanel)
        return settings.captcha_validated_fields or tuple()

    def set_captcha_validated_fields(self, allowed_types):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ICaptchaSettingsControlPanel)
        settings.captcha_validated_fields = allowed_types

    captcha_validated_fields = property(get_captcha_validated_fields,
                                        set_captcha_validated_fields)
