from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

    name = forms.CharField(
        max_length=255,
        help_text="Please enter your full name"
    )
    email = forms.EmailField(
        help_text="We will only use your email to respond to your inquiry"
    )
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        help_text="Enter your phone number (optional)"
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        help_text="Please type your message or inquiry here"
    )
