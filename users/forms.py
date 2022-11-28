from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full rounded-md dark:bg-neutral-800 dark:text-white dark:placeholder:text-white dark:border-white dark:focus:border-none",
                "placeholder": "Username",
            }
        )
    )
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full rounded-md dark:bg-neutral-800 dark:text-white dark:placeholder:text-white dark:border-white dark:focus:border-none",
                "placeholder": "Full Name",
            }
        ),
        max_length=32,
        help_text="Full Name",
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "w-full rounded-md dark:bg-neutral-800 dark:text-white dark:placeholder:text-white dark:border-white dark:focus:border-none",
                "placeholder": "Email",
            }
        ),
        max_length=64,
        help_text="Enter a valid email address",
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full rounded-md dark:bg-neutral-800 dark:text-white dark:placeholder:text-neutral-200",
                "placeholder": "Password",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full rounded-md dark:bg-neutral-800 dark:text-white dark:placeholder:text-neutral-200",
                "placeholder": "Confirm Password",
            }
        )
    )

    class Meta(UserCreationForm.Meta):
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
        )
