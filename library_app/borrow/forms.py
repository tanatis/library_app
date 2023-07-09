from django import forms

from library_app.borrow.models import Borrow


class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ()
