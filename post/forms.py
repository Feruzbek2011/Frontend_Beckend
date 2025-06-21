from django import forms
from .models import Post, Comments
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'summary', 'body', 'photo')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control border-success',
                'aria-describedby': "basic-addon1"
            }),
            'summary': forms.Textarea(attrs={
                'class': 'form-control border-success',
                'aria-describedby': "basic-addon1"
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control border-success',
                'aria-describedby': "basic-addon1"
            }),
            'photo': forms.TextInput(attrs={
                'role': 'uploadcare-uploader',
                'data-clearable': 'true',
                'class': 'form-control border-success',
                'id': "uploadcare-photo"
            }),
        }

class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'summary', 'body', 'photo')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control border-warning',
                'placeholder': 'Sarlavhani tahrirlang'
            }),
            'summary': forms.TextInput(attrs={
                'class': 'form-control border-warning',
                'placeholder': 'Yangi qisqacha mazmun'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control border-warning',
                'rows': 6,
                'placeholder': 'Matnni o‘zgartiring'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control border-warning'
            }),
        }


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'comment')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control border-success',
                'placeholder': 'Ismingiz'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control border-success',
                'rows': 3,
                'placeholder': 'Komment yozing...'
            }),
        }


class PostCommentEditForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'comment')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control border-warning',
                'placeholder': 'Ismni tahrirlang'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control border-warning',
                'rows': 3,
                'placeholder': 'Kommentni o‘zgartiring'
            }),
        }
