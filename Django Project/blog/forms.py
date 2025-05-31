# blog/forms.py

from django import forms
from django import forms
from .models import Post, Category


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )

class PostForm(forms.ModelForm):

    # Multiple select for existing categories
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )
    # New category text input
    new_category = forms.CharField(
        max_length=100,
        required=False,
        help_text="Enter a new category if not in the list"
    )


    class Meta:
        model = Post
        fields = ['title', 'body', 'image', 'video', 'categories']