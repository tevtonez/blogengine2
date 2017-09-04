from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
  class Meta():
    model = Post
    fields = ('author', 'title', 'text')

    widgets = {
      'title':forms.TextInput(attrs={'class':'text-input-class'}),
      'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea post-content'}),
    }


class CommentForm(forms.ModelForm):
  class Meta():
    model = Comment
    fields = ('author', 'text')

    widgets = {
      'author':forms.TextInput(attrs={'class':'text-input-class'}),
      'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
    }
