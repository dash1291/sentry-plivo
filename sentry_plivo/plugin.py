from django import forms
from django.utils.translation import ugettext_lazy as _
from sentry.plugins.bases.notify import NotificationPlugin

import plivo


class PlivoConfForm(forms.Form):
    auth_id = forms.CharField(label=_('Auth ID'), required=True,
        widget=forms.TextInput(attrs={'class': 'span6'}))
    auth_token = forms.CharField(label=_('Auth Token'), required=True,
        widget=forms.PasswordInput(render_value=True, attrs={'class': 'span6'}))
    sender = forms.CharField(label=_('Sender #'), required=True,
        help_text=_('Digits only'),
        widget=forms.TextInput(attrs={'placeholder': 'e.g. 3305093095'}))
    recipient = forms.CharField(label=_('Recipient #'), required=True,
        help_text=_('Recipient phone number'),
        widget=forms.TextInput(attrs={'placeholder': '5555555555'}))


class PlivoPlugin(NotificationPlugin):
    author = 'Ashish Dubey'
    author_url = 'https://github.com/dash1291'
    version = '0.1'
    description = 'A Sentry plugin for sending SMS notifications via Plivo.'

    slug = 'plivo'
    title = _('Plivo')
    conf_title = title
    conf_key = 'plivo'
    project_conf_form = PlivoConfForm

    def notify_users(self, group, event):
        project = group.project

        body = 'Sentry [{0}] {1}: {2}'.format(
            project.name.encode('utf-8'),
            event.get_level_display().upper().encode('utf-8'),
            event.error().encode('utf-8').splitlines()[0]
        )
        body = body[:160]

        auth_id = self.get_option('auth_id', project)
        auth_token = self.get_option('auth_token', project)
        sender = self.get_option('sender', project)
        recipient = self.get_option('recipient', project)

        p = plivo.RestAPI(auth_id, auth_token)
        p.send_message({
            'src': sender,
            'dst': recipient,
            'text': body
        })
