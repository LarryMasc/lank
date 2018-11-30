from django import forms

from .models import email_data


class send_msg_form(forms.ModelForm):
        sender = forms.EmailField(label="Sender", widget=forms.TextInput(
                attrs={
                        "placeholder": "larry.masc@gmail.com",
                }
        ))
        class Meta:
                model = email_data
                fields = [
                    'sender',
                    'recipient',
                    'subject',
                    'body',
                    'cc_myself',
                ]
        def clean_sender(self, *args, **kwargs):
                sender = self.cleaned_data.get("sender")
                if not "larry.masc@gmail.com" in sender:
                        raise forms.ValidationError("Sender can only be larry.masc@gmail.com")
                return sender

# class send_msg_form(forms.Form):
#         sender = forms.EmailField(label="Sender")
#         recipient = forms.EmailField(label="Recipient")
#         subject = forms.CharField(label="Subject")
#         body = forms.CharField(label="Message",
#                                widget=forms.Textarea(
#                                        attrs={
#                                                "class": "new-class-name two",
#                                                "rows": 24,
#                                                "cols": 80,
#                                        }
#                                ))
#         cc_myself = forms.BooleanField(required=False)
