from django import forms
from .models import *


class ChatForm(forms.Form):
    TEMPCHOICES = (('5','TEMPERATURE'),('1','0.1'),('2','0.2'),('3','0.3'),('4','0.4'),('5','0.5'),('6','0.6'),('7','0.7'),('8','0.8'),('9','0.9'),('10','1.0'))
    CONTEXTCHOICES = (('YES','CONTEXT'),('YES','YES'),('NO','NO'))
    temperature = forms.ChoiceField(choices=TEMPCHOICES, widget=forms.Select(attrs=
        {'class': 'select-temp w-node-b91f7330-36d2-bf4e-fc1a-d66e8233fbd4-9d78feda w-select',
         'id': 'field-2',
         'name': 'temperature',
         'placeholder': 'TEMPERATURE',
         'data-name':'Temperature'
         }),required=False)

    context = forms.ChoiceField(choices=CONTEXTCHOICES, widget=forms.Select(attrs=
    {'class': 'select-temp w-node-b91f7330-36d2-bf4e-fc1a-d66e8233fbd4-14932c8f w-select',
     'id': 'field-2',
     'name': 'context',
     'placeholder': 'CONTEXT',
     'data-name': 'Context'
     }),required=False)

    answer = forms.CharField(widget=forms.Textarea(attrs=
    {'class': '',
     'id': 'name',
     'name': 'answer',
     'data-name': 'Answer',
     'style': 'border:none; outline:none; border-style:none; border-color:Transparent; overflow:auto; opacity: 1;',
     'rows':2
     }),required=False)

    response = forms.CharField(widget=forms.Textarea(attrs={
        'style': 'width:450px; border:none; outline:none; border-style:none; border-color:Transparent; overflow:auto; opacity: 1;',
        # 'rows': 2,
    }))
    question = forms.CharField(widget=forms.TextInput(attrs=
    {'class': 'subscribe-form-input w-node-_67e93785-6278-b925-a661-4f92cae5470d-9d78feda w-input',
     'maxlength' : '10000',
     'placeholder': 'QUESTION',
     'id': 'Subscriber-Email-2',
     'name': 'question',
     'data-name': 'Question'
     }),required=False)