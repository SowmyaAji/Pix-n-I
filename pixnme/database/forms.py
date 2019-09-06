from django import forms
from database.models import Post


class UpdatePostForm(forms.ModelForm):

    class Meta:

        model = Post
        fields = ('imgURL', 'caption')
