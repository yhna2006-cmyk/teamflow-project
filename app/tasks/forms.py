from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Task
        fields = ['title', 'assignee', 'deadline']
