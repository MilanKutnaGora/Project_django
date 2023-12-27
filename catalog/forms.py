from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'image', 'price',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        bad_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in bad_word:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Недопустимые слова')

            return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        bad_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in bad_word:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Недопустимые слова')

            return cleaned_data