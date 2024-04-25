from django import forms
from .models import Booking
from .models import BookingRequest


class StudentLoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'exampleInputEmail'}))
    password = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'type': 'password', 'id': 'exampleInputPassword'}))

class LecturerLoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'exampleInputEmail'}))
    password = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'type': 'password', 'id': 'exampleInputPassword'}))

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['lecturer', 'unit', 'day', 'time_slot']

class BookingRequestForm(forms.ModelForm):        
 class Meta:
        model = BookingRequest
        fields = ['lecturer', 'unit', 'day', 'time_slot']