from django import forms

class ContactForm(forms.Form):
    sender = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"span3","placeholder":"type your name here ..",'size':'40'}))
    