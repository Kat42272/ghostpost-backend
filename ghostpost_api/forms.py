from django import forms
from .models import Post

class PostForm(forms.Form):
  post = forms.CharField(max_length=200)
  post_choices = forms.ChoiceField(choices=(
    (True, 'Boast'),
    (False, 'Roast'),
  ))