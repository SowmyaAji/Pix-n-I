from database.models import Post
from django import forms


class UpdatePostForm(forms.ModelForm):
    caption = forms.CharField(label="Caption", widget=forms.TextInput(attrs={'class': 'form-control', }
                                                                      ))
    imgURL = forms.CharField(label="imgURL", widget=forms.TextInput(attrs={'class': 'form-control', }
                                                                    ))

    class Meta:

        model = Post
        fields = ('imgURL', 'caption')
