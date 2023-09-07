from django.forms import ModelForm, TextInput, Textarea

from toys.models import Category


class AddBookForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        # widgets = {
        #     'title': TextInput(attrs={'class': "form-control"}),
        #     "text": Textarea(attrs={'class': "form-control"})
        # }