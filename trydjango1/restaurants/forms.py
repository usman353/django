from django import forms
from .models import RestaurantLocation
# from .validators import validate_categories


class RestaurantCreateForms(forms.Form):
    name = forms.CharField()
    location = forms.CharField(required=False)
    categories = forms.CharField(required=False)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'Hello':
            raise forms.ValidationError('Not a valid name')
        return name


class RestaurantLocationCreateForms(forms.ModelForm):
    # categories = forms.CharField(validators=[validate_categories], required=False)
    # email = forms.EmailField()

    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'categories'
        ]

    def clean_name(self):  # clean_ is the default method with the variable name to validate
        name = self.cleaned_data.get('name')
        if name == 'Hello':
            raise forms.ValidationError('Not a valid name')
        return name

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if 'edu' in email:
    #         raise forms.ValidationError('Not allowed domain')
    #     return email
