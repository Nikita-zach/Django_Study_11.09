from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'date', 'time', 'people', 'message')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Your Name',
                'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 4 chars'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'Your Email',
                'data-rule': 'email',
                'data-msg': 'Please enter a valid email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'phone',
                'placeholder': 'Your Phone',
                'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 4 chars'
            }),
            'date': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'date',
                'placeholder': 'Date',
                'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 4 chars'
            }),
            'time': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'time',
                'placeholder': 'Time',
                'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 4 chars'
            }),
            'people': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'people',
                'placeholder': '# of people',
                'data-rule': 'minlen:1',
                'data-msg': 'Please enter at least 1 chars'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '5',
                'placeholder': 'Message'
            }),
        }

        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'date': 'Reservation Date',
            'time': 'Reservation Time',
            'people': 'Number of People',
            'message': 'Message (Optional)',
        }

        error_messages = {
            'name': {
                'min_length': 'Please enter at least 4 characters for the name.',
                'required': 'Name is required.',
            },
            'email': {
                'invalid': 'Please enter a valid email address.',
                'required': 'Email is required.',
            },
            'phone': {
                'min_length': 'Please enter at least 4 characters for the phone number.',
                'required': 'Phone number is required.',
            },
            'date': {
                'invalid': 'Please enter a valid date.',
                'required': 'Reservation date is required.',
            },
            'time': {
                'invalid': 'Please enter a valid time.',
                'required': 'Reservation time is required.',
            },
            'people': {
                'min_value': 'Please enter at least 1 person.',
                'required': 'Number of people is required.',
            },
            'message': {
                'max_length': 'Your message is too long. Maximum 500 characters allowed.',
            },
        }
