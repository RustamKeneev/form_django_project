from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=20, min_length=2, error_messages={
        'max_length': 'Слишком много символов',
        'min_length': 'Слишком мало символов',
        'required': 'Укажите хотябы 2 символа',
    })
    surname = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))
    rating = forms.IntegerField(label="Рейтинг", max_value=5, min_value=1)
