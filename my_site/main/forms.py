# main/forms.py
from django import forms

class ColorTestForm(forms.Form):
    question_1 = forms.ChoiceField(
        choices=[('1', 'Option 1'), ('2', 'Option 2')],
        widget=forms.RadioSelect,
        label="Question 1"
    )
    question_2 = forms.ChoiceField(
        choices=[('1', 'Option A'), ('2', 'Option B')],
        widget=forms.RadioSelect,
        label="Question 2"
    )
