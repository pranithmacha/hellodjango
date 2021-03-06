from django import forms

class ContactForm(forms.Form):
    sender = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"span3","placeholder":"type your message here ..","cols":"80","rows":"5"}))
    