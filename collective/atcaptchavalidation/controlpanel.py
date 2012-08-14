# -*- coding: utf-8 -*-

from plone.protect import CheckAuthenticator
from plone.app.controlpanel.form import ControlPanelForm
from plone.registry.interfaces import IRegistry
from zope import schema
from zope.component import adapts, getMultiAdapter, getUtility
from zope.formlib import form
from zope.interface import Interface, implements

from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.statusmessages.interfaces import IStatusMessage

from collective.atcaptchavalidation import captchavalidationMessageFactory as _


class ICaptchaSettingsControlPanel(Interface):

    captcha_validated_fields = schema.Tuple(
        title=_(u"captcha_settings_title",
                default=u"Portal types that may use captcha validation"),
        description=_(u"captcha_settings_help",
                      default=u"Select portal types that should be captcha validated"),
        missing_value=tuple(),
        value_type=schema.Choice(vocabulary="plone.app.vocabularies.UserFriendlyTypes"),
        required=False
    )


class CaptchaSettingsControlPanel(ControlPanelForm):

    implements(ICaptchaSettingsControlPanel)
    form_fields = form.FormFields(ICaptchaSettingsControlPanel)
    label = _(u"atcaptchavalidation_form_title",
              default=u'AT settings for captcha field')
    description = _(u"atcaptchavalidation_form_description",
                    default=u'Select here which kind of object should be capthca validated')
    form_name = _(u"atcaptchavalidation_form_name",
                  default=u'AT Captcha validation settings')

    @form.action(_(u'Save'), name=u'save')
    def handle_edit_action(self, action, data):
        CheckAuthenticator(self.request)
        if form.applyChanges(self.context, self.form_fields, data,
                             self.adapters):
            self.status = _('atcaptchavalidation_form_action_change_saved',
                            default=u"Changes saved.")
            self._on_save(data)
        else:
            self.status = _('atcaptchavalidation_form_action_no_change',
                            default=u"No changes made.")

    @form.action(_(u'Cancel'), name=u'cancel')
    def handle_cancel_action(self, action, data):
        IStatusMessage(self.request).addStatusMessage(
            _(u"atcaptchavalidation_form_action_change_cancelled",
              default=u"Changes canceled."), type="info")
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
