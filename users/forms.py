from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import Profile
from chirps.models import Chirp


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full rounded-md dark:bg-neutral-800 dark:text-white dark:placeholder:text-white dark:border-white dark:focus:border-none",
                "autocomplete": "off",
                "autofocus": "true",
                "placeholder": "First Name",
            }
        ),
        max_length=32,
        help_text="First Name",
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full rounded-md dark:bg-neutral-800 dark:text-white dark:placeholder:text-white dark:border-white dark:focus:border-none",
                "autocomplete": "off",
                "placeholder": "Last Name",
            }
        ),
        max_length=32,
        help_text="Last Name",
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full rounded-md dark:bg-neutral-800 dark:text-white dark:placeholder:text-white dark:border-white dark:focus:border-none",
                "autocomplete": "off",
                "placeholder": "Username",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "w-full rounded-md dark:bg-neutral-800 dark:text-white dark:placeholder:text-white dark:border-white dark:focus:border-none",
                "autocomplete": "off",
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


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "w-full rounded-md dark:bg-neutral-800 dark:text-white dark:placeholder:text-white dark:border-white dark:focus:border-none",
                "autocomplete": "off",
                "autofocus": "true",
                "placeholder": "Username",
            }
        ),
        max_length=150,
        help_text="Username",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full rounded-md dark:bg-neutral-800 dark:text-white dark:placeholder:text-white dark:border-white dark:focus:border-none",
                "autofocus": "true",
                "placeholder": "Password",
            }
        ),
        max_length=150,
        help_text="Password",
    )

    class Meta:
        model = User
        fields = ("username", "password")

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError(
                "Sorry, that login was invalid. Please try again."
            )
        return self.cleaned_data


class ChangeUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(
                                     attrs={
                                         "class": "w-full rounded-md dark:bg-neutral-800 dark:text-white dark:placeholder:text-white dark:border-white dark:focus:border-none",
                                         "autocomplete": "off",
                                         "placeholder": "First Name",
                                     }
                                 )
                                 )
    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(
                                    attrs={
                                        "class": "w-full rounded-md dark:bg-neutral-800 dark:text-white dark:placeholder:text-white dark:border-white dark:focus:border-none",
                                        "autocomplete": "off",
                                        "placeholder": "Last Name",
                                    }
                                )
                                )
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(
                                   attrs={
                                       "class": "w-full rounded-md dark:bg-neutral-800 dark:text-white dark:placeholder:text-white dark:border-white dark:focus:border-none",
                                       "autocomplete": "off",
                                       "placeholder": "Username",
                                   }
                               )
                               )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',)


class ChangeProfileForm(forms.ModelForm):
    bio = forms.CharField(max_length=100,
                          widget=forms.TextInput(
                              attrs={
                                  "class": "w-full rounded-md dark:bg-neutral-800 dark:text-white dark:placeholder:text-white dark:border-white dark:focus:border-none",
                                  "autocomplete": "off",
                                  "placeholder": "Bio",
                              }
                          )
                          )

    class Meta:
        model = Profile
        fields = ('bio',)


class CreateChirpForm(forms.ModelForm):
    content = forms.CharField(max_length=100,
                              widget=forms.Textarea(
                                  attrs={
                                      "class": "w-full rounded-md dark:bg-neutral-800 dark:text-white dark:placeholder:text-white dark:border-white dark:focus:border-none",
                                      "autocomplete": "off",
                                      "placeholder": "What is Happening?",
                                  }
                              )
                              )

    class Meta:
        model = Chirp
        fields = ('content',)
