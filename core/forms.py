from django import forms
from .models import AdmissionApplication
import phonenumbers


def get_country_code_choices():
    codes = set()
    for region in phonenumbers.SUPPORTED_REGIONS:
        code = phonenumbers.country_code_for_region(region)
        if code:
            codes.add((f"+{code}", f"+{code} ({region})"))
    return sorted(codes)


COUNTRY_CODE_CHOICES = get_country_code_choices()


class AdmissionApplicationForm(forms.ModelForm):

    phone_country_code = forms.ChoiceField(
        choices=COUNTRY_CODE_CHOICES,
        initial="+91",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = AdmissionApplication
        fields = "__all__"

    def clean_certificates(self):
        file = self.cleaned_data.get('certificates', False)
        if file:
            if not file.name.endswith('.pdf'):
                raise forms.ValidationError("Only PDF files are allowed.")
        return file

class StudentLoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-input"}
        ),
    )
    password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-input"}
        ),
    )
