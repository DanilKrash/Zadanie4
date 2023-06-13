from django import forms
from django.forms import TextInput, Textarea, CheckboxInput

from news.models import Comment, Record


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'author': TextInput(attrs={
                'class': 'comment_holder',
                'placeholder': 'Автор',
            }),
            'text': Textarea(attrs={
                'class': 'comment_holder',
                'placeholder': 'Текст',
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('name', 'text', 'image', 'logo', 'hidden')
        widgets = {
            'name': TextInput(attrs={
                'class': 'comment_holder',
                'placeholder': 'Название',
            }),
            'text': Textarea(attrs={
                'class': 'comment_holder',
                'placeholder': 'Текст',
            }),
            'hidden': CheckboxInput(attrs={
                'value': 'Опубликовать',
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""