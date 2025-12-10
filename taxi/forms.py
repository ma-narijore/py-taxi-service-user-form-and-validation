from django import forms
from .models import Driver, Car
import re


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        value = self.cleaned_data["license_number"]

        pattern = r"^[A-Z]{3}\d{5}$"

        if not re.match(pattern, value):
            raise forms.ValidationError(
                "License number must have 3 uppercase letters followed by 5 digits. Example: ABC12345"
            )

        return value


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=Driver.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Car
        fields = "__all__"
