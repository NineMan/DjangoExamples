from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)               # имя читающего пост
    email = forms.EmailField()                          # электронка читающего пост
    to = forms.EmailField()                             # кому отправить рекомендацию
    comments = forms.CharField(required=False,
                              widget=forms.Textarea)    # комментарии в письме


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
