from django.forms import ModelForm, Textarea
from .models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['body',]
        widgets = {
            'body': Textarea(attrs={'class': 'editor-form'})
        }
