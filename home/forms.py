
from django import forms
from django.forms import ModelForm
from home.models import History



class HistoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['disc'].widget.attrs.update(
            {
                'class': 'form-control', 
                'placeholder': 'Write your medical history here...'
            }
        )

    class Meta:
        model = History
        fields = ('disc',)

        labels = {
            'disc': 'History'
        }
        Widget = {
            'disc': forms.Textarea(),
        } 