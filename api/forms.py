from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    text = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'placeholder': 'Post', 'class': 'form-control'}))
    post_type = forms.BooleanField(default=True)

    class Meta:
        model = Post
        fields = ['text', 'post_type']