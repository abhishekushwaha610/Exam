from django import forms
from .models import Question
from tinymce import TinyMCE

class Question_form(forms.Form):
    content = forms.CharField(widget=TinyMCE(mce_attrs={'width': "100%","height":'150px'}),label="")

class Question_content(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("question",)
