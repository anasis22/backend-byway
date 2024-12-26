from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ["username","email", "password", "password_confirm"]

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        # Check for existing username
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("A user with this username already exists.")
        
        # Check if email exists
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")

        # Compare password and password_confirm
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
