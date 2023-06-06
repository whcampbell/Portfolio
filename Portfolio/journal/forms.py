from django import forms

class CommentForm(forms.Form) :
    body = forms.CharField(max_length=512, required=True, widget=forms.Textarea, label='Write a Comment')
