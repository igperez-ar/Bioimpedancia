from django import forms

class SignUpForm(UserCreationForm):
     = forms.CharField(max_length=30, required=True)
    surnames = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
