from django import forms
from database.models import Post


class UpdatePostForm(forms.ModelForm):
    caption = forms.CharField(label="Caption", widget=forms.TextInput(attrs={'class': 'form-control', }
                                                                      ))

    class Meta:

        model = Post
        fields = ('imgURL', 'caption')
