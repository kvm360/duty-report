from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Shift, PTORequest, TeamMember
import pytz

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['member', 'title', 'start_time_utc', 'end_time_utc', 'notes']
        widgets = {
            'member': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Shift Title'}),
            'start_time_utc': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_time_utc': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Optional notes'}),
        }

class PTORequestForm(forms.ModelForm):
    class Meta:
        model = PTORequest
        fields = ['start_date', 'end_date', 'reason']
        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Reason for leave'}),
        }

class TeamMemberForm(forms.ModelForm):
    timezone = forms.ChoiceField(
        choices=[(tz, tz) for tz in pytz.all_timezones],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = TeamMember
        fields = ['timezone']
