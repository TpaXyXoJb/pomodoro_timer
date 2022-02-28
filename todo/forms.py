from django import forms

from todo.models import Task, Loop


class TaskCreationForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': "tasks-new__name tasks-input-name", 'placeholder': "Название"}))
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "tasks-new__description tasks-input-description", 'placeholder': "Описание"}))

    class Meta:
        model = Task
        fields = ['title', 'description']


class TaskUpdateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': "tasks-edit__name tasks-input-name", 'placeholder': "Новое название"}))
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "tasks-edit__description tasks-input-description", 'placeholder': "Описание"}))
    is_finished = forms.CheckboxInput()

    class Meta:
        model = Task
        fields = ['title', 'description', 'is_finished']


class LoopCreateForm(forms.ModelForm):
    duration = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': "input-pom-minutes"}))
    timeout = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': "input-big-break"}))
    rounds = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': "input-rounds"}))
    short_timeout = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': "input-small-break"}))

    class Meta:
        model = Loop
        fields = ['duration', 'timeout', 'rounds', 'short_timeout']
