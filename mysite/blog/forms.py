from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)               # имя читающего пост
    email = forms.EmailField()                          # электронка читающего пост
    to = forms.EmailField()                             # кому отправить рекомендацию
    comments = forms.CharField(required=False,
                              widget=forms.Textarea)    # комментарии в письме
