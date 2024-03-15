import re
from django import forms


class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
        ]
    )
    delivery_adress = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", 'False'),
            ("1", 'True'),
        ]
    )


    def clean_phone_number(self):
        """
        A function to clean and validate a phone number input, raising a ValidationError if the phone number is not in the correct format.
        """
        data = self.cleaned_data['phone_number']

        if not data.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры')

        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(data):
            raise forms.ValidationError('Неверный формат номера телефона')

        return data
