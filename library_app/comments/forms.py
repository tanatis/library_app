from django import forms

from library_app.comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'placeholder': 'Add comment...',
                    'class': 'lib-form-input',
                })
        }
