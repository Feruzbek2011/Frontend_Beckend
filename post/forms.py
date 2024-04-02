from .models import Post, Comments
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title', 'summary', 'body', 'photo')

        widgets = {
            'title': forms.TextInput(attrs={'type':'text', 'class': 'form-control border-success', 'aria-describedby':"basic-addon1"}),
            'summary': forms.TextInput(attrs={'type':'text', 'class': 'form-control border-success', 'aria-describedby':"basic-addon1"}),
            'photo': forms.FileInput(attrs={'class': 'form-control border-success', 'id':"inputGroupSelect01"}),
            # 'author': forms.Select(attrs={'class': "form-select border-success", 'id':"inputGroupSelect01"}),
        }
class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title', 'summary', 'body', 'photo',)

        widgets = {
            'title': forms.TextInput(attrs={'type':'text', 'class': 'form-control border-warning', 'aria-describedby':"basic-addon1"}),
            'summary': forms.TextInput(attrs={'type':'text', 'class': 'form-control border-warning', 'aria-describedby':"basic-addon1"}),
            'photo': forms.FileInput(attrs={'class': 'form-control border-warning', 'id':"inputGroupSelect01"}),
        }
class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields=('name', 'comment')

        widgets = {
            'name': forms.TextInput(attrs={'type':'text', "placeholder":"Commentni qisqa mazmuni yoki nomini kiriting.", 'class': 'form-control border-success', 'aria-describedby':"basic-addon1"}),
        }

class PostCommentEditForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields=('name', 'comment')

        widgets = {
            'name': forms.TextInput(attrs={'type':'text', 'class': 'form-control border-warning', 'aria-describedby':"basic-addon1"}),
        }
