
from .models import *
from django import forms


#########################





class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body','email')
        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Enter your Name or Username','class':'form-control'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter your email to submit', 'class':'form-control'}),
            'body':forms.Textarea(attrs={ 'placeholder':'Write Comment Here','class':'form-control'}),
            
        }
