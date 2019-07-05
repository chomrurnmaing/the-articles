from django import forms

from pages.models import Post


class NewsForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(required=False)

    class Meta:
        model = Post
        fields = ['title', 'content']
