from django import forms
from chirps.models import Chirp


class CreateChirpForm(forms.ModelForm):
    content = forms.CharField(max_length=280,
                              widget=forms.Textarea(
                                  attrs={
                                      "class": "w-full rounded-md dark:bg-neutral-800 dark:text-white dark:placeholder:text-white resize-none",
                                      "rows": "2",
                                      "placeholder": "What is Happening?",
                                      "x-model": "content"  # alpine.js
                                  }
                              )
                              )

    class Meta:
        model = Chirp
        fields = ('content',)

class EditChirpForm(forms.ModelForm):
    content = forms.CharField(max_length=280,
                              widget=forms.Textarea(
                                  attrs={
                                      "class": "w-full rounded-md dark:bg-neutral-800 dark:text-white dark:placeholder:text-white resize-none",
                                      "rows": "2",
                                      "placeholder": "What is Happening?",
                                      "x-model": "content"  # alpine.js
                                  }
                              )
    )

    class Meta:
        model = Chirp
        fields = ('content',)
