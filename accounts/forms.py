from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control input-perso'}),
        max_length=100,
        error_messages={'invalid': ("Email invalid.")})

    password1 = forms.CharField(
        label="Password",
        # max_length=50, min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'form-control input-perso'})
    )

    password2 = forms.CharField(
        label="Password Confirmation",
        # max_length=50, min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password Again', 'class': 'form-control input-perso'})
    )

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        exclude = ['username']

    def clean_email(self):
        user_email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=user_email)
        except User.DoesNotExist:
            return user_email
        raise forms.ValidationError(u'Username "%s" is already in use.' % user_email)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise ValidationError(message)

        return password2

    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)

        # automatically set to email address to create a unique identifier
        instance.username = instance.email

        if commit:
            instance.save()

        return instance


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
