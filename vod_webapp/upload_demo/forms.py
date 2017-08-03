from django import forms


class UploadForm(forms.Form):
    demog_file = forms.FileField()

