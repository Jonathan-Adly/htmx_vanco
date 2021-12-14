from django import forms


class VancoForm(forms.Form):
    INDICATION_CHOICES = [
        ("empiric", "Empiric"),
        ("bacteremia", "Bacteremia"),
        ("cellulitis", "Cellulitis"),
        ("endocarditis", "Endocarditis"),
        ("meningitis", "Meningitis"),
        ("osteomyelitis", "Osteomyelitis"),
        ("pneumonia", "Pneumona"),
        ("sepsis", "Sepsis"),
        ("surgical", "Surgical prophylaxis"),
    ]
    GOAL_CHOICES = [("15-20", "15-20 mcg/mL"), ("10-15", "10-15 mcg/mL")]

    actual_body_weight = forms.IntegerField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Actual Body Weight"}),
    )
    indication = forms.ChoiceField(choices=INDICATION_CHOICES, required=True)
    goal_trough = forms.ChoiceField(choices=GOAL_CHOICES, required=True)
    crcl = forms.IntegerField(
        required=True, label="", widget=forms.TextInput(attrs={"placeholder": "CrCl"})
    )


class CrCLForm(forms.Form):
    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]
    age = forms.IntegerField(
        required=True, widget=forms.NumberInput(attrs={"placeholder": "Age"})
    )
    height = forms.IntegerField(
        required=True, widget=forms.NumberInput(attrs={"placeholder": "Height"})
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, required=True, widget=forms.RadioSelect, label=""
    )
    scr = forms.DecimalField(
        max_digits=4,
        decimal_places=2,
        required=True,
    )
    weight = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={"placeholder": "Actual Body Weight"}),
    )
