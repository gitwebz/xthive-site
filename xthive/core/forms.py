from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-3 mb-4 bg-teal-700 text-white rounded', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-3 mb-4 bg-teal-700 text-white rounded', 'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'w-full p-3 mb-4 bg-teal-700 text-white rounded h-32', 'placeholder': 'Your Message'}),
        }